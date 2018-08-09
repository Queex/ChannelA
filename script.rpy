# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.


label start:

    # sanity check - because of the random paths, errors introduced are not apparent
    # unless that branch is picked, so run each function once to make sure those
    # errors are found at startup
    python:
        make_character()
        make_character_list()
        make_adjective()
        make_place()
        make_team()
        make_adventure(False)
        make_mood_piece(False)
        make_slice_of_life(False)
        make_backdrop()
        make_coda()
        make_anime()
        
        
label repeat:

    scene screen

    $ tmp=make_anime()
    $ sell=make_sell()
    "[sell]{p=1.0}\n{size=+20}[tmp]{/size}{w=5.0}{nw}"
    
    
    jump repeat
    
    
init python:

    def make_sell():
        sell=['Okay, but what about:', "Here's a great idea:",
                'This one will shift merchandise:',
                "It's coming to me... it's coming to me...", 'The focus group came up with:',
                'This year the kids are all about:', 'Hear me out on this:',
                'So this is a million-yen idea:', 'Just spitballing here, but:',
                "We've secured the rights to:", 'Hold onto your hats, how about:',
                'Umm... we could do this:', 'Market research suggests:',
                "Sure, but this one's a guaranteed winner:",
                'The networks insist we get this one:']
                
        return renpy.random.choice(sell)

    def apply_a(str):
        if str[:1].isupper():
            str=str
        elif str[:1] in ['a','e','i','o','u']:
            str="an "+str
        else:
            str="a "+str
        return str

    def make_character():
        
        characters_a=['boy','girl','man','woman','schoolkid']
        characters_b=['maid','vampire','superhero','robot',
                'ninja','pirate','sorcerer','warrior','hunter','mercenary','spaceship captain',
                'godly being','class representative','teacher','salaryman','assassin',
                'traveller','psychic','investigator','cop','ghost','cyborg','pop idol',
                'shrine maiden','witch','wizard','necromancer','hacker','mech pilot',
                'chef','ice skater','footballer','racing driver','transfer student',
                'mad scientist','mobster','hoodlum','private eye','oracle','dragon','king',
                'queen','prince','princess','gunslinger','gambler','teacher','dog','cat',
                'lawyer','cowboy']
                
        # 10% of list a, 90% of list b
        # 50% of adjective
        
        if renpy.random.random()<0.5:
            adjective=make_adjective()+" "
        else:
            adjective=""
            
        if renpy.random.random()<0.1:
            char=renpy.random.choice(characters_a)
        else:
            char=renpy.random.choice(characters_b)
            
        tmp="%s%s" % (adjective, char)
        tmp=apply_a(tmp)
            
        return tmp
        
    def make_adjective():
    
        adjectives=['young','old','sexy','cross-dressing','mysterious','amoral','moe',
                'foul mouthed','ditzy','stern','violent','incompetent','style conscious',
                'bisexual','monster','cat-eared','bunny-eared','mostly nude','pun-making',
                'invincible','hyperintelligent','drill-haired','bald','fourth-wall-breaking',
                'cryptic','inexplicable','heavy drinking','chain smoking','short','creepy',
                'chronically ill','pink-haired','invisible','deep-voiced','quiet','shy',
                'blank-eyed','loud','yampy','giant','undead','evil','lolita fashion',
                'aroused','faceless','jail bait','fetishwear','flying','cosplaying','angry',
                'sleepy','masked', 'singing','wise-cracking','improbably proportioned',
                'cool','fish-eyed']
                
        return renpy.random.choice(adjectives)
        
    def make_character_list():
    
        # 60% single, 30% secondary, 10% team 
        primary=make_character()
        
        tmp=renpy.random.random()
        if tmp<0.3:
            extra=" and "+make_character()
            plural=True
        elif tmp<0.4:
            extra=" and their "+make_team()
            plural=True
        else:
            extra=""
            plural=False
            
        return ("%s%s" % (primary,extra),plural)
        
    def make_team():
        teams=['orchestra','fan club','family','children','parents','siblings','pets',
                'pet monsters','furby','hallucinations','ancestor ghosts','future self',
                'dance troupe','neighbours','bros','friends','polyamorous collective',
                'dragon','flying machine','dope ride','horse','cheese','sunglasses','lover',
                'posse','harem', 'mime troupe','hat','younger brother','older sister',
                'chaperone','intestinal parasite']
                
        # 25% adjective
        if renpy.random.random()<0.25:
            adjective=make_adjective()+" "
        else:
            adjective=""
        
        team=renpy.random.choice(teams)
        
        return "%s%s" % (adjective,team)
        
    def make_adventure(plural):
        
        place_verbs=['defend','destroy','burn','join','conquer','rediscover','rule',
                'redecorate','visit','enter']
        person_verbs=['rescue','resurrect','kidnap',('marry','marries'),'seduce',
                'insult','slap',
                ("'accidentally' undress","'accidentally' undresses"), 'rob', 'humiliate']
        both_verbs=['defeat','find',('spy on','spies on'), 'investigate','awaken','photograph']
        directives=['must','ISARE chosen by destiny to','HAVEHAS made it their goal to',
                'setSINGULARS out to','makeSINGULARS plans to',
                'ISARE helplessly swept up in a conspiracy to',
                'HAVEHAS no choice but to', 'through no fault of their own manageSINGULARS to',
                'just wantSINGULARS some tea but endSINGULARS up forced to',
                'makeSINGULARS a wish to', 'fulfilSINGULARS an ancient prophecy to',
                'beatSINGULARS incredible odds to', 'dareSINGULARS to']
                
        if plural:
            opts=('are','have','')
        else:
            opts=('is','has','s')
            
        # 50% person, 50% place
        if renpy.random.random() < 0.5:
            obj=make_character()
            verb=renpy.random.choice(person_verbs+both_verbs)
        else:
            obj=make_place()
            verb=renpy.random.choice(place_verbs+both_verbs)
            
        # 30% no directive
        if renpy.random.random() < 0.3:
            directive=renpy.random.choice(directives)
            if isinstance(verb, tuple):
                verb=verb[0] # turn tuple back into scalar
            out= "%s %s %s" % (directive, verb, obj)
        else:
            # Need to deal with plural gubbins here
            verb=verbulate(verb,plural)
            out="%s %s" % (verb, obj)
            
        out=out.replace('ISARE',opts[0]).replace('HAVEHAS',opts[1])
        out=out.replace('SINGULARS',opts[2])
        return out
    
    def verbulate(vin, plural):
        if isinstance(vin, tuple):
            if plural:
                out=vin[0]
            else:
                out=vin[1]
        else:
            if not plural:
                tmp=vin.split(' ')
                tmp[0]=tmp[0]+'s'
                out=" ".join(tmp)
            else:
                out=vin
        return out
    
    def make_place():
            
        places=['bus shelter','castle','country','mountain','island paradise','fortress',
                'office block','Warwick University', 'tower', 'boat', 'train', 'labyrinth',
                'temple', 'village', 'city', 'country', 'dimension', 'galaxy',
                'anime convention','Coventry','wardrobe','dungeon','school','club room',
                'bedroom','family home','place of work','apartment complex',
                'magical realm']
        adjectives=['heavily defended','closely guarded','haunted','abandoned','lost',
                'evil','very evil','flying','corporate','extravagantly evil','curious',
                'mythical','legendary','purple','ruined','zombie-infested','forbidden',
                'deadly','dreary','messy']
        # 50% chance of place adjective, 25% chance of person adjective
        tmp=renpy.random.random()
        if tmp < 0.5:
            adjective=renpy.random.choice(adjectives)+" "
        elif tmp < 0.75:
            adjective=make_adjective()+" "
        else:
            adjective=""
            
        return apply_a("%s%s" % (adjective,renpy.random.choice(places)))
        
    def make_mood_piece(plural):
        
        verbs=['contemplate',('discuss','discusses'),
                ('indulge in long internal monologues about',
                    'indulges in long internal monologues about'),'debate',
                ('reflect on','reflects on'),
                ('recover memories of','recovers memories of'),
                'ponder', 'lament', 'analyse','probe the nature of']
        topics=['past failures','existence','futility','sex','history','clothes',
                'war','death','joy','hopelessness','cheese','cars','sports','violence',
                'love','nothing','random algorithmic generation','panty shots','memes',
                'language','puns','clothes','funeral customs','loss','bowel ants']
        
        verb=renpy.random.choice(verbs)
        topic=renpy.random.choice(topics)
        backdrop = make_backdrop()
        verb=verbulate(verb,plural)
        return "%s %s %s" % (verb, topic, backdrop)
    
    def make_backdrop():
        links=['against a backdrop of','in front of blurred images of',
                'while the camera lingers lovingly on still pictures of',
                'during a time of','during a lecture about',
                'while music plays that puts you in mind of',
                'in front of grainy photographs of','while in the background a TV shows']
        backdrops=['flowers','war','Tokyo','geometric shapes','tasteful sepia nudes',
                'nightmare fuel','clouds','dead flowers','children playing','books','food',
                'the ocean','rain','snow','cheese','war crimes','depressing urban skylines',
                'fire','the night sky','origami']
        link=renpy.random.choice(links)
        backdrop=renpy.random.choice(backdrops)
        return "%s %s" % (link, backdrop)
    
    def make_slice_of_life(plural):
        
        actions=['make friends','learn about life',('laugh together','laughs alone'),
                'earn money','banter','grow up','achieve their dreams','find happiness',
                'overcome loss','play games','tell jokes','mock politics',
                'make lots and lots of puns', 'tell ridiculous stories',
                'fall in and out of love', 'come out of the closet','get arrested',
                ('just about get by','just about gets by'),
                "make pop culture references that don't age well", 'perform slapstick comedy',
                'crack wise','lampoon society','tell dirty jokes','work hard','play hard',
                'cosplay',('watch anime', 'watches anime'), 'sigh heavily', 'learn about history',
                'learn about science', 'drink heavily',
                ('slowly melt into a pile of dogs','slowly melts into a pile of dogs')]
        
        # Get two actions, reduce down to 1 if the same.
        action1=renpy.random.choice(actions)
        action2=renpy.random.choice(actions)
        if action1==action2:
            full_action=verbulate(action1,plural)
        else:
            full_action=verbulate(action1,plural)+" and "+verbulate(action2,plural)
            
        # 75% chance of place, 25% chance of backdrop
        if renpy.random.random() <0.75:
            place="in "+make_place()
        else:
            place=make_backdrop()
        
        return "%s %s" % (full_action, place)
    
    def make_fanservice(plural):
        
        deliveries_own=['show off their', 'titillate the viewers using their',
                'deliver loving close-ups of their',
                ('obligingly display their','obligingly displays their'),
                ("won't stop stroking their","won't stop stroking their"),
                "keep 'accidentally' exposing their",
                ('are just there to show off their','is just there to show off their'),
                'fight monsters using magic that for some reason exposes their',
                'emphasise their ample', 'derive their true power from']
        deliveries_other=['get nosebleeds looking at','wander past an endless cavalcade of',
                'surf the internet looking for',
                ('watch anime featuring','watches anime featuring'),
                'get into hilarious scrapes trying to get a glimpse of',
                'court trouble in pursuit of',
                ('embarrass themselves over', 'embarrasses themselves over'),
                ('are part of a cult that worships','is part of a cult that worships')]
        services=['boobs','panties','blessed thiccness','shapely rearSINGULARS', 'underboob',
                'cleavage','armpits','gayness','swimsuits','thigh-high stockings',
                'absolute territory','leather boots','figure-hugging bodysuits',
                'oiled torsoSINGULARS','belly buttonSINGULARS','underwear','braSINGULARS',
                'buttocks','nipples','feet','crotchular regionSINGULARS','tongueSINGULARS']
                
        delivery=renpy.random.choice(deliveries_own+deliveries_other)
        service=renpy.random.choice(services)
        
        if plural or delivery in deliveries_other:
            opts=('s','')
        else:
            opts=('','')
            
        delivery=verbulate(delivery, plural)
            
        out='%s %s' % (delivery, service)
        out=out.replace('SINGULARS',opts[0])
        
        return out
            
    
    def make_coda():
    
        codas=['set in the future','set in the past',"everyone's actually dead",
                'set after the apocalypse',
                'set in feudal Japan','set in space','set under the sea',
                "everyone's dead and in hell",
                "everyone's dead and in limbo",
                'with aliens',"everyone's a mascot",
                'done through interpretive dance','dubbed into Welsh',
                'played for comedy','as a series of two minute web shorts',
                'courting the stoner audience','created just for the merchandising',
                'backwards','hardcore pornography','in black and white','a Netflix original',
                'it ends halfway through with no resolution','hyperactive',
                "everyone's a furry", 'ruined during localisation',
                'with egregious product placement','who cares?',
                'with shockingly bad tween frames','pointlessly censored']
        
        out= renpy.random.choice(codas)
        return out
    
    def make_anime():
    
        char_list=make_character_list()
        
        # 50% adventure, 25% slice of life, 15% fanservice, 10% mood piece
        tmp=renpy.random.random()
        if tmp < 0.15:
            plot=make_fanservice(char_list[1])
        elif tmp < 0.65:
            plot=make_adventure(char_list[1])
        elif tmp < 0.9:
            plot=make_slice_of_life(char_list[1])
        else:
            plot=make_mood_piece(char_list[1])
            
        # 5% chance of coda
        if renpy.random.random()<0.05:
            coda=" (but "+make_coda()+")."
        else:
            coda="."
        
        out= "%s %s%s" % (char_list[0],plot,coda)
        out=out[0].upper()+out[1:]
        return out
        