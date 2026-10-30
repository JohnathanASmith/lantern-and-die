import json,os,glob,sys
R=os.path.dirname(__file__)+'/repo/'
SD=R+'sheet_definitions/'
def find(name):
    m=glob.glob(SD+'**/'+name+'.json',recursive=True)
    return m[0] if m else None
ITEMS={ # slot: [names]
 'body':['body'],
 'head':['heads_human_male','heads_human_female','heads_human_male_elderly','heads_human_female_elderly','heads_human_child','heads_human_male_gaunt','heads_human_male_plump','heads_orc_male','heads_orc_female','heads_goblin','heads_lizard_male','heads_lizard_female','heads_troll','heads_minotaur','heads_wolf_male','heads_boarman'],
 'ears':['head_ears_elven','head_ears_medium','head_ears_big','head_ears_long'],
 'hair':['hair_plain','hair_messy1','hair_messy','hair_parted','hair_pixie','hair_bangs','hair_page','hair_unkempt','hair_bedhead','hair_long','hair_long_messy','hair_long_straight','hair_wavy','hair_wavy_child','hair_loose','hair_braid','hair_ponytail','hair_high_ponytail','hair_topknot_long','hair_bangs_bun','hair_half_up','hair_parted_side_bangs','hair_relm_xlong'],
 'beard':['beards_beard','beards_medium','beards_trimmed','beards_winter','beards_5oclock_shadow'],
 'shirt':['torso_clothes_longsleeve','torso_clothes_shortsleeve','torso_clothes_sleeveless','torso_clothes_tunic','torso_clothes_blouse','torso_clothes_blouse_longsleeve','torso_clothes_robe','torso_clothes_child_shirt','torso_clothes_longsleeve_laced'],
 'dress':['dress_bodice','dress_sash'],
 'over':['torso_jacket_tabard','torso_jacket_frock','torso_jacket_collared','torso_clothes_vest','torso_aprons_apron','torso_aprons_overalls','torso_armour_leather','torso_armour_plate','torso_armour_legion','torso_chainmail','torso_clothes_corset'],
 'belt':['belt_leather'],
 'cape':['cape_solid','cape_tattered'],
 'legs':['legs_pants','legs_pantaloons','legs_skirts_plain','legs_skirt_belle','legs_childpants','legs_childskirts','legs_widepants','legs_armour'],
 'feet':['feet_boots_basic','feet_shoes_basic','feet_boots_fold','feet_armour'],
 'hat':['hat_hood_cloth','hat_magic_wizard','hat_helmet_nasal','hat_helmet_barbarian','hat_helmet_kettle','hat_helmet_greathelm','hat_helmet_mail','hat_helmet_horned'],
 'weapon':['weapon_sword_longsword','weapon_sword_arming','weapon_sword_dagger','weapon_sword_rapier','weapon_sword_saber','weapon_blunt_mace','weapon_blunt_waraxe','weapon_blunt_club','weapon_polearm_spear','weapon_polearm_halberd','weapon_magic_simple','weapon_magic_gnarled','weapon_magic_wand','weapon_ranged_crossbow','weapon_ranged_bow_normal','weapon_ranged_slingshot'],
 'shield':['shield_kite','shield_round','shield_heater_wood','shield_spartan'],
}
KEEP=['black','blue','brown','gray','green','red','white','purple','leather','tan','maroon','forest','navy','charcoal','walnut','sky','dark brown','light gray','yellow','orange','teal','pink']
BODIES=['male','female','muscular','child']
plan={};paths=set();missing=[]
for slot,names in ITEMS.items():
    for n in names:
        f=find(n)
        if not f: missing.append(n);continue
        d=json.load(open(f))
        it={'slot':slot,'name':d.get('name',n),'layers':[],'recolors':None,'variants':None}
        rc=d.get('recolors')
        if rc:
            if 'material' in rc: it['recolors']=[{'material':rc['material'],'base':rc.get('base')}]
            else: it['recolors']=[{'material':v.get('material'),'base':v.get('base')} for k,v in sorted(rc.items()) if k.startswith('color_')]
        else:
            vs=d.get('variants',[]);keep=[v for v in KEEP if v in vs][:12] or vs[:6]
            it['variants']=keep
        for k in sorted([k for k in d if k.startswith('layer_')]):
            L=d[k]
            if 'custom_animation' in L: continue
            for b in BODIES:
                p=L.get(b)
                if not p or '${' in p: continue
                if it['recolors'] is not None: files={'':'spritesheets/'+p+'walk.png'}
                else: files={v:'spritesheets/'+p+'walk/'+v.replace(' ','_')+'.png' for v in it['variants']}
                for x in files.values(): paths.add(x)
                it['layers'].append({'z':L.get('zPos',0),'body':b,'files':files})
        plan[n]=it
bw='spritesheets/weapon/ranged/bow/normal/walk/'
plan['weapon_ranged_bow_normal']={'slot':'weapon','name':'Bow','recolors':None,'variants':['bow'],'layers':[{'z':-1,'body':b,'files':{'bow':bw+'background.png'}} for b in ('male','female','muscular')]+[{'z':140,'body':b,'files':{'bow':bw+'foreground.png'}} for b in ('male','female','muscular')]}
paths.update([bw+'background.png',bw+'foreground.png'])
json.dump(plan,open(os.path.dirname(__file__)+'/plan.json','w'))
open(os.path.dirname(__file__)+'/paths.txt','w').write('\n'.join(sorted(paths)))
print(len(plan),'items',len(paths),'files; missing',missing)
