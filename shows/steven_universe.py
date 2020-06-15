#! /usr/bin/env python3
# -*- coding: utf-8 -*-

from show_continuity import *

'''Data on the show Steven Universe.'''
show = Show(
    title='Steven Universe',
    # Season colors from https://en.wikipedia.org/wiki/List_of_Steven_Universe_episodes
    seasons={
        1: {'color': '#FF5E6D',
            'episodes': {
                'S1E1': 'Gem Glow',
                'S1E2': 'Laser Light Cannon',
                'S1E3': 'Cheeseburger Backpack',
                'S1E4': 'Together Breakfast',
                'S1E5': 'Frybo',
                'S1E6': 'Cat Fingers',
                'S1E7': 'Bubble Buddies',
                'S1E8': 'Serious Steven',
                'S1E9': 'Tiger Millionaire',
                'S1E10': "Steven's Lion",
                'S1E11': 'Arcade Mania',
                'S1E12': 'Giant Woman',
                'S1E13': 'So Many Birthdays',
                'S1E14': 'Lars and the Cool Kids',
                'S1E15': 'Onion Trade',
                'S1E16': 'Steven the Sword Fighter',
                'S1E17': 'Lion 2: The Movie',
                'S1E18': 'Beach Party',
                'S1E19': "Rose's Room",
                'S1E20': 'Coach Steven',
                'S1E21': 'Joking Victim',
                'S1E22': 'Steven and the Stevens',
                'S1E23': 'Monster Buddies',
                'S1E24': 'An Indirect Kiss',
                'S1E25': 'Mirror Gem',
                'S1E26': 'Ocean Gem',
                'S1E27': 'House Guest',
                'S1E28': 'Space Race',
                'S1E29': 'Secret Team',
                'S1E30': 'Island Adventure',
                'S1E31': 'Keep Beach City Weird',
                'S1E32': 'Fusion Cuisine',
                'S1E33': "Garnet's Universe",
                'S1E34': 'Watermelon Steven',
                'S1E35': 'Lion 3: Straight to Video',
                'S1E36': 'Warp Tour',
                'S1E37': 'Alone Together',
                'S1E38': 'The Test',
                'S1E39': 'Future Vision',
                'S1E40': 'On the Run',
                'S1E41': 'Horror Club',
                'S1E42': 'Winter Forecast',
                'S1E43': 'Maximum Capacity',
                'S1E44': 'Marble Madness',
                'S1E45': "Rose's Scabbard",
                'S1E46': 'Open Book',
                'S1E47': 'Shirt Club',
                'S1E48': 'Story for Steven',
                'S1E49': 'The Message',
                'S1E50': 'Political Power',
                'S1E51': 'The Return',
                'S1E52': 'Jail Break'}},
        2: {'color': '#91ECDD',
            'episodes': {
                'S2E1': 'Full Disclosure',
                'S2E2': 'Joy Ride',
                'S2E3': 'Say Uncle',
                'S2E4': 'Love Letters',
                'S2E5': 'Reformed',
                'S2E6': 'Sworn to the Sword',
                'S2E7': 'Rising Tides, Crashing Skies',
                'S2E8': 'Keeping It Together',
                'S2E9': 'We Need to Talk',
                'S2E10': 'Chille Tid',
                'S2E11': 'Cry for Help',
                'S2E12': 'Keystone Motel',
                'S2E13': 'Onion Friend',
                'S2E14': 'Historical Friction',
                'S2E15': 'Friend Ship',
                'S2E16': 'Nightmare Hospital',
                'S2E17': "Sadie's Song",
                'S2E18': 'Catch and Release',
                'S2E19': 'When It Rains',
                'S2E20': 'Back to the Barn',
                'S2E21': 'Too Far',
                'S2E22': 'The Answer',
                'S2E23': "Steven's Birthday",
                'S2E24': "It Could've Been Great",
                'S2E25': 'Message Received',
                'S2E26': 'Log Date 7 15 2'}},
        3: {'color': '#B895D1',
            'episodes': {
                'S3E1': 'Super Watermelon Island',
                'S3E2': 'Gem Drill',
                'S3E3': 'Same Old World',
                'S3E4': 'Barn Mates',
                'S3E5': 'Hit the Diamond',
                'S3E6': 'Steven Floats',
                'S3E7': 'Drop Beat Dad',
                'S3E8': 'Mr. Greg',
                'S3E9': 'Too Short to Ride',
                'S3E10': 'The New Lars',
                'S3E11': 'Beach City Drift',
                'S3E12': 'Restaurant Wars',
                'S3E13': "Kiki's Pizza Delivery Service",
                'S3E14': 'Monster Reunion',
                'S3E15': 'Alone at Sea',
                'S3E16': 'Greg the Babysitter',
                'S3E17': 'Gem Hunt',
                'S3E18': 'Crack the Whip',
                'S3E19': 'Steven vs. Amethyst',
                'S3E20/21': 'Bismuth',
                'S3E22': 'Beta',
                'S3E23': 'Earthlings',
                'S3E24': 'Back to the Moon',
                'S3E25': 'Bubbled'}},
        4: {'color': '#A12766',
            'episodes': {
                'S4E1': 'Kindergarten Kid',
                'S4E2': 'Know Your Fusion',
                'S4E3': "Buddy's Book",
                'S4E4': 'Mindful Education',
                'S4E5': 'Future Boy Zoltron',
                'S4E6': 'Last One Out of Beach City',
                'S4E7': 'Onion Gang',
                'S4E8/9': 'Gem Harvest',
                'S4E10': 'Three Gems and a Baby',
                'S4E11': "Steven's Dream",
                'S4E12': 'Adventures in Light Distortion',
                'S4E13': 'Gem Heist',
                'S4E14': 'The Zoo',
                'S4E15': 'That Will Be All',
                'S4E16': 'The New Crystal Gems',
                'S4E17': 'Storm in the Room',
                'S4E18': 'Rocknaldo',
                'S4E19': 'Tiger Philanthropist',
                'S4E20': 'Room for Ruby',
                'S4E21': 'Lion 4: Alternate Ending',
                'S4E22': 'Doug Out',
                'S4E23': 'The Good Lars',
                'S4E24': 'Are You My Dad?',
                'S4E25': 'I Am My Mom',
            }},
        5: {'color': '#ACDF7D',
            'episodes': {
                'S5E1': 'Stuck Together',
                'S5E2': 'The Trial',
                'S5E3': 'Off Colors',
                'S5E4': "Lars' Head",
                'S5E5': 'Dewey Wins',
                'S5E6': 'Gemcation',
                'S5E7': 'Raising the Barn',
                'S5E8': 'Back to the Kindergarten',
                'S5E9': 'Sadie Killer',
                'S5E10': 'Kevin Party',
                'S5E11': 'Lars of the Stars',
                'S5E12': 'Jungle Moon',
                'S5E13': 'Your Mother and Mine',
                'S5E14': 'The Big Show',
                'S5E15': 'Pool Hopping',
                'S5E16': 'Letters to Lars',
                'S5E17': "Can't Go Back",
                'S5E18': 'A Single Pale Rose',
                'S5E19': "Now We're Only Falling Apart",
                'S5E20': "What's Your Problem",
                'S5E21': 'The Question',
                'S5E22': 'Made of Honor',
                'S5E23/24': 'Reunited',
                'S5E25': 'Legs From Here to Homeworld',
                'S5E26': 'Familiar',
                'S5E27': 'Together Alone',
                'S5E28': 'Escapism',
                'S5E29-32': 'Change Your Mind'}}})

show.plot_threads = [
    ('S1E1', 'S1E23', Plot.CAUSAL, 'Centipeedle arc'),
    ('S1E23', 'S3E14', Plot.CAUSAL, 'Centipeedle arc'),
    ('S3E14', 'S5E25', Plot.CAUSAL, 'Centipeedle arc'),
    ('S1E3', 'S1E38', Plot.CAUSAL, 'Sea Spire test'),
    ('S1E9', 'S4E19', Plot.CAUSAL, "Steven/Amethyst's underground wrestling careers"),
    ('S1E10', 'S1E17', Plot.CAUSAL, "Steven's pet Lion"),
    ('S1E17', 'S1E35', Plot.CAUSAL, "Mystery of Lion's mane"),
    ('S1E35', 'S1E45', Plot.CAUSAL, "Lion's mane-dimension"),
    ('S1E17', 'S1E45', Plot.CAUSAL, "Steven having seen Rose's Sword/Armory"),
    ('S1E24', 'S1E26', Plot.REFERENTIAL, "Steven's healing power"),
    ('S1E24', 'S1E27', Plot.REFERENTIAL, "Steven's healing power"),
    ('S1E27', 'S3E14', Plot.CAUSAL, "Loss of Steven's healing power"),
    ('S1E25', 'S1E26', Plot.SERIAL, 'Lapis arc'),
    ('S1E26', 'S1E49', Plot.CAUSAL, 'Lapis arc'),
    ('S1E26', 'S1E27', Plot.CAUSAL, "Greg's broken leg"),
    ('S1E28', 'S1E36', Plot.CAUSAL, 'Galaxy warp checking/sticker'),
    ('S1E34', 'S3E1', Plot.CAUSAL, 'Watermelon Stevens'),
    ('S1E35', 'S4E21', Plot.CAUSAL, "Rose's tape for Steven"),
    ('S1E35', 'S5E4', Plot.CAUSAL, "Mystery of Lion's nature"),
    ('S1E36', 'S1E44', Plot.SERIAL, 'Peridot arc'),
    ('S1E37', 'S3E11', Plot.CAUSAL, "Stevonnie's run-in with Kevin"),
    ('S1E37', 'S5E10', Plot.CAUSAL, "Stevonnie's run-in with Kevin"),
    ('S1E39', 'S1E42', Plot.CAUSAL, "Garnet's future vision"),
    ('S1E44', 'S1E49', Plot.CAUSAL, 'Homeworld gems invasion arc'),
    ('S1E49', 'S1E50', Plot.CAUSAL, 'Homeworld gems invasion arc'),
    ('S1E49', 'S1E51', Plot.CAUSAL, 'Homeworld gems invasion arc'),
    ('S1E51', 'S1E52', Plot.SERIAL, 'Homeworld gems invasion arc'),
    ('S1E52', 'S2E1', Plot.CAUSAL, 'Homeworld gems invasion arc'),
    ('S1E52', 'S2E22', Plot.CAUSAL, '"We were waiting for your birthday"'),
    ('S1E48', 'S2E9', Plot.CAUSAL, 'Rose/Greg flashback arc'),
    ('S1E48', 'S3E16', Plot.CAUSAL, 'Rose/Greg flashback arc'),
    ('S1E52', 'S2E10', Plot.CAUSAL, 'Malachite arc'),
    ('S2E10', 'S3E1', Plot.SERIAL, 'Malachite arc'),
    ('S1E52', 'S2E2', Plot.CAUSAL, 'Peridot hunt arc'),
    ('S2E2', 'S2E8', Plot.CAUSAL, 'Peridot hunt arc'),
    ('S2E8', 'S2E11', Plot.SERIAL, 'Peridot hunt arc'),
    ('S2E11', 'S2E15', Plot.SERIAL, 'Peridot hunt arc'),
    ('S2E15', 'S2E18', Plot.SERIAL, 'Peridot hunt arc'),
    ('S1E45', 'S2E16', Plot.REFERENTIAL, "Rose's Sword"),
    ('S2E6', 'S2E16', Plot.CAUSAL, "Connie's training"),
    ('S2E6', 'S3E17', Plot.CAUSAL, "Connie's training"),
    ('S1E44', 'S2E8', Plot.CAUSAL, 'Gem mutants experiment released by Peridot'),
    ('S2E8', 'S2E16', Plot.CAUSAL, 'Gem mutants'),
    ('S2E11', 'S2E12', Plot.SERIAL, 'Sardonyx arc'),
    ('S2E12', 'S2E15', Plot.SERIAL, 'Sardonyx arc'),
    ('S1E52', 'S2E18', Plot.CAUSAL, 'Cluster arc'),
    ('S2E18', 'S2E19', Plot.SERIAL, 'Cluster arc'),
    ('S2E8', 'S2E19', Plot.REFERENTIAL, 'Gem Mutants'),
    ('S2E19', 'S2E20', Plot.CAUSAL, 'Cluster arc'),
    ('S2E20', 'S2E21', Plot.CAUSAL, 'Cluster arc'),
    ('S1E13', 'S2E23', Plot.CAUSAL, "Steven's age fluctuation arc"),
    ('S2E20', 'S2E24', Plot.CAUSAL, 'Cluster arc'),
    ('S2E20', 'S2E25', Plot.REFERENTIAL, "Peridot's giant robot"),
    ('S2E24', 'S2E25', Plot.SERIAL, 'Peridot/Diamond communicator arc'),
    ('S2E24', 'S3E1', Plot.CAUSAL, 'Cluster arc'),
    ('S3E1', 'S3E2', Plot.SERIAL, 'Cluster arc'),
    ('S2E8', 'S3E2', Plot.REFERENTIAL, 'Gem Mutants'),
    ('S3E1', 'S3E3', Plot.CAUSAL, 'Lapis redemption arc'),
    ('S3E3', 'S3E4', Plot.SERIAL, 'Lapis/Peridot barn arc.'),
    ('S3E4', 'S3E5', Plot.SERIAL, 'Rubies arc'),
    ('S1E48', 'S3E7', Plot.CAUSAL, "Greg/Marty's contract"),
    ('S3E7', 'S3E8', Plot.CAUSAL, "Greg's fortune"),
    ('S3E1', 'S3E15', Plot.CAUSAL, 'Jasper/Lapis arc'),
    ('S3E7', 'S3E15', Plot.CAUSAL, "Greg's fortune"),
    ('S3E15', 'S3E17', Plot.CAUSAL, 'Jasper arc'),
    ('S3E17', 'S3E18', Plot.CAUSAL, 'Jasper arc'),
    ('S3E18', 'S3E19', Plot.CAUSAL, 'Amethyst self-worth arc'),
    ('S1E35', 'S3E20/21', Plot.CAUSAL, "Bismuth's gem"),
    ('S3E18', 'S3E22', Plot.CAUSAL, 'Jasper arc'),
    ('S3E19', 'S3E22', Plot.CAUSAL, 'Amethyst self-worth arc'),
    ('S3E22', 'S3E23', Plot.SERIAL, 'Jasper arc'),
    ('S3E5', 'S3E24', Plot.CAUSAL, 'Rubies arc'),
    ('S3E23', 'S3E24', Plot.SERIAL, "Rubies' arrival"),
    ('S3E23', 'S3E24', Plot.CAUSAL, 'RQ killed PD arc'),
    ('S3E24', 'S3E25', Plot.SERIAL, 'Rubies arc'),
    ('S3E23', 'S4E2', Plot.CAUSAL, 'Smoky Quartz arc'),
    ('S4E11', 'S4E12', Plot.SERIAL, 'Zoo arc'),
    ('S4E12', 'S4E13', Plot.SERIAL, 'Zoo arc'),
    ('S4E13', 'S4E14', Plot.SERIAL, 'Zoo arc'),
    ('S4E14', 'S4E15', Plot.SERIAL, 'Zoo arc'),
    ('S4E12', 'S4E16', Plot.CAUSAL, "Crystal Gems' absence"),
    ('S3E25', 'S4E20', Plot.CAUSAL, 'Rubies arc - Navy'),
    ('S1E44', 'S4E22', Plot.CAUSAL, 'List of humans Steven gave Peridot'),
    ('S4E15', 'S4E22', Plot.CAUSAL, 'BD wanting to save some humans'),
    ('S4E22', 'S4E23', Plot.CAUSAL, 'Disappearing townies arc'),
    ('S4E23', 'S4E24', Plot.SERIAL, 'Disappearing townies arc'),
    ('S4E24', 'S4E25', Plot.SERIAL, 'Disappearing townies arc'),
    ('S4E25', 'S5E1', Plot.SERIAL, 'Steven/Lars on Homeworld arc'),
    ('S3E20/21', 'S5E2', Plot.CAUSAL, 'Steven assuming Rose used Breaking Point'),
    ('S3E24', 'S5E2', Plot.CAUSAL, 'RQ killed PD arc + Eyeball'),
    ('S5E1', 'S5E2', Plot.SERIAL, 'Steven/Lars on Homeworld arc'),
    ('S5E2', 'S5E3', Plot.SERIAL, 'Steven/Lars on Homeworld arc'),
    ('S5E3', 'S5E4', Plot.SERIAL, 'Steven/Lars on Homeworld arc'),
    ('S4E25', 'S5E5', Plot.CAUSAL, "Townies' concern with handling of gem events"),
    ('S4E25', 'S5E5', Plot.CAUSAL, 'Steven/Connie fight arc'),
    ('S5E5', 'S5E6', Plot.SERIAL, 'Steven/Connie fight arc'),
    ('S5E2', 'S5E7', Plot.CAUSAL, 'Lapis leaving arc'),
    ('S5E7', 'S5E8', Plot.CAUSAL, 'Lapis leaving arc - Peridot'),
    ('S5E6', 'S5E10', Plot.SERIAL, 'Steven/Connie fight arc'),
    ('S5E4', 'S5E11', Plot.CAUSAL, 'Lars/Off Colors arc'),
    ('S5E11', 'S5E12', Plot.SERIAL, 'Stranded arc'),
    ('S5E9', 'S5E14', Plot.CAUSAL, 'Sadie Killer arc'),
    ('S5E5', 'S5E16', Plot.CAUSAL, 'Dewey having lost his job'),
    ('S5E9', 'S5E16', Plot.CAUSAL, 'New Big Donut employee needed'),
    ('S5E7', 'S5E17', Plot.CAUSAL, 'Lapis leaving arc'),
    ('S5E16', 'S5E17', Plot.CAUSAL, "Ronaldo's lookout duty"),
    ('S5E6', 'S5E18', Plot.CAUSAL, "Pearl's unspeakable secret arc"),
    ('S5E17', 'S5E18', Plot.CAUSAL, 'Memory/Vision of Pearl'),
    ('S5E18', 'S5E19', Plot.CAUSAL, 'RQ=PD aftermath arc - Sapphire'),
    ('S5E18', 'S5E20', Plot.CAUSAL, 'RQ=PD aftermath arc - Amethyst'),
    ('S5E18', 'S5E21', Plot.CAUSAL, 'RQ=PD aftermath arc - Ruby'),
    ('S3E20/21', 'S5E22', Plot.CAUSAL, 'Bismuth arc'),
    ('S5E21', 'S5E22', Plot.SERIAL, 'Ruby/Sapphire wedding arc'),
    ('S3E2', 'S5E23/24', Plot.CAUSAL, "Steven's friendship with the Cluster"),
    ('S5E17', 'S5E23/24', Plot.CAUSAL, 'Lapis leaving arc'),
    ('S5E22', 'S5E23/24', Plot.SERIAL, 'Ruby/Sapphire wedding arc'),
    ('S4E21', 'S5E25', Plot.CAUSAL, "Pink's ship"),
    ('S5E23/24', 'S5E25', Plot.SERIAL, 'Diamonds/Steven arc'),
    ('S5E25', 'S5E26', Plot.SERIAL, 'Diamonds/Steven Homeworld arc'),
    ('S5E26', 'S5E27', Plot.SERIAL, 'Diamonds/Steven Homeworld arc'),
    ('S5E27', 'S5E28', Plot.SERIAL, 'Diamonds/Steven Homeworld arc'),
    ('S5E28', 'S5E29-32', Plot.SERIAL, 'Diamonds/Steven Homeworld arc')]

show.foreshadowing = [
    ('S1E1', 'S1E52', Foreshadowing.MAJOR, 'Two shooting stars in OP when Garnet appears; Garnet fusion'),
    ('S1E1', 'S1E12', Foreshadowing.MAJOR, 'Temple statue; Existence of fusion'),
    ('S1E1', 'S1E26', Foreshadowing.MAJOR, 'Monsters have gems; Monsters are corrupted gems'),
    ('S1E1', 'S1E7', Foreshadowing.MINOR, 'Bracelet in freezer; setting up for Connie intro'),
    ('S1E1', 'S1E52', Foreshadowing.MAJOR, 'Garnet having two gems; Garnet fusion'),
    ('S1E1', 'S1E26', Foreshadowing.MAJOR, 'Cookie cat song: "came to this planet from outer space"; Gems are aliens'),
    ('S1E1', 'S5E18', Foreshadowing.MAJOR, 'Cookie cat song: "pet for your tummy", "left his family behind"; RQ=PD'),
    ('S1E1', 'S1E26', Foreshadowing.MAJOR, 'Pearl: "Properties of this planet"; Gems are aliens'),
    ('S1E2', 'S1E39', Foreshadowing.MAJOR, 'Garnet adjusts glasses then announces only way to destroy Red Eye; Future vision'),
    ('S1E2', 'S1E17', Foreshadowing.MINOR, '"You\'ve gotta know where it is... Like a cave dungeon"; Rose\'s armory'),
    ('S1E2', 'S1E16', Foreshadowing.MINOR, '"...or a cloud fortress"; Sky Arena'),
    ('S1E3', 'S1E13', Foreshadowing.MINOR, '"You should have seen it in its heyday"; Gems\' age'),
    ('S1E3', 'S1E26', Foreshadowing.MAJOR, '"Oasis for gems on earth"; Gems are aliens'),
    ('S1E3', 'S1E39', Foreshadowing.MAJOR, 'Garnet senses danger several times while adjusting glasses; Future vision'),
    ('S1E4', 'S1E19', Foreshadowing.MAJOR, "Glimpse of Rose's Room"),
    ('S1E4', 'S1E52', Foreshadowing.MAJOR, 'Garnet has two door lights; Garnet fusion'),
    ('S1E6', 'S1E9', Foreshadowing.MINOR, 'Amethyst shapeshifts briefly into Purple Puma'),
    ('S1E7', 'S5E29-32', Foreshadowing.MINOR, "Temple statue (Obsidian)'s sword visible in ocean"),
    ('S1E8', 'S1E40', Foreshadowing.MAJOR, '"This was once a gem battlefield"; Gem rebellion'),
    ('S1E8', 'S2E24', Foreshadowing.MAJOR, 'Rose vs diamonds mural; Existence of diamond authority'),
    ('S1E9', 'S5E18', Foreshadowing.MAJOR, '"that\'s why we\'re all here... to be wild and free... and make up nicknames"; RQ=PD'),
    ('S1E10', 'S1E35', Foreshadowing.MAJOR, 'Lion is pink; Lion belonging to Rose'),
    ('S1E10', 'S5E18', Foreshadowing.MAJOR, 'Pet lion; royalty symbolism; RQ=PD'),
    ('S1E10', 'S1E40', Foreshadowing.MAJOR, '"We kept Amethyst"; Amethyst\'s origin'),
    ('S1E11', 'S1E39', Foreshadowing.MAJOR, '"Heightened senses", third eye symbolism; Future vision'),
    ('S1E11', 'S1E51', Foreshadowing.MINOR, '"fighting a giant foot"; homeworld invasion hand ship'),
    ('S1E11', 'S1E52', Foreshadowing.MAJOR, "Garnet's third eye; Garnet fusion"),
    ('S1E13', 'S1E16', Foreshadowing.MAJOR, '"even if your [...] body\'s an illusion"; Gems\' bodies being light constructs'),
    ('S1E13', 'S5E18', Foreshadowing.MAJOR, 'Crown/cape; royalty symbolism; RQ=PD'),
    ('S1E14', 'S1E17', Foreshadowing.MINOR, 'Dogcopter 3 poster in background'),
    ('S1E16', 'S1E26', Foreshadowing.MAJOR, 'Gems poof same as monsters; Monsters are corrupted gems'),
    ('S1E16', 'S1E39', Foreshadowing.MAJOR, 'Garnet anticipates Steven raising his hand; Future vision'),
    ('S1E16', 'S5E18', Foreshadowing.MAJOR, "Diamond on Holo-Pearl's chest; Pearl belonged to PD"),
    ('S1E17', 'S5E4', Foreshadowing.MAJOR, 'Lion can walk on water like Jesus; Lion was resurrected'),
    ('S1E17', 'S5E18', Foreshadowing.MAJOR, 'Giant penny; batman; secret identity; RQ=PD'),
    ('S1E19', 'S1E35', Foreshadowing.MINOR, "Tiny Floating Pink Whale has Rose's voice"),
    ('S1E19', 'S2E24', Foreshadowing.MAJOR, "Simulated Beach City's stars are White, Blue, Yellow, and Pink diamonds; Existence of Diamond Authority"),
    ('S1E22', 'S1E26', Foreshadowing.MAJOR, 'Flashforward of ocean disappearance'),
    ('S1E22', 'S1E52', Foreshadowing.MAJOR, "Garnet playing keytar ('fusion' instrument); Garnet fusion"),
    ('S1E23', 'S1E26', Foreshadowing.MAJOR, 'Centipeedle humanoid stage while reforming; Monsters are corrupted gems'),
    ('S1E23', 'S1E52', Foreshadowing.MAJOR, '"Shut down by the G-squad"; Garnet fusion'),
    ('S1E28', 'S5E18', Foreshadowing.MAJOR, "Pink diamond on Pearl's spacesuit; Pearl belonged to PD"),
    ('S1E31', 'S2E24', Foreshadowing.MAJOR, '"They\'re here to hollow out the earth"; Gem plans for Earth'),
    ('S1E31', 'S2E24', Foreshadowing.MAJOR, '"It\'s all part of the great diamond authority"; Existence of Diamond Authority'),
    ('S1E31', 'S5E12', Foreshadowing.MAJOR, "Upside down diamond on currency; Pink Diamond's design"),
    ('S1E31', 'S5E18', Foreshadowing.MAJOR, "Pearl's aversion to shape-shifting; Pearl's role in PD's 'shattering'"),
    ('S1E32', 'S1E52', Foreshadowing.MAJOR, 'Ruby/Sapphire outlines briefly visible while Alexandrite unfusing; Garnet fusion'),
    ('S1E33', 'S1E52', Foreshadowing.MAJOR, '"He\'s not ready to learn that I have secret animal friends"; Garnet fusion'),
    ('S1E34', 'S5E18', Foreshadowing.MAJOR, 'Watermelon crown; royalty symbolism; RQ=PD'),
    ('S1E36', 'S1E40', Foreshadowing.MAJOR, '"They\'re coming back! I can\'t do this, not again!"; Gem rebellion'),
    ('S1E36', 'S1E40', Foreshadowing.MAJOR, '"Preparing to locate and manually reactivate Kindergar-"; Kindergarten(s)'),
    ('S1E37', 'S1E52', Foreshadowing.MAJOR, '"Fusion is really hard, even for us." "Not for me"; Garnet fusion'),
    ('S1E39', 'S1E40', Foreshadowing.MAJOR, '"Cookie Cat! [...] I never considered that you would be evil!"; Gems hurt the planet'),
    ('S1E43', 'S1E51', Foreshadowing.MAJOR, 'Jasper appears on totem pole in U-Stor; Jasper'),
    ('S1E43', 'S3E4', Foreshadowing.MAJOR, '"Season 3... that\'s when the uptight neighbors the Richingtons move next-door"; Peridot/Lapis moving into barn'),
    ('S1E44', 'S4E8/9', Foreshadowing.MINOR, '"I swear that\'s not his real name."; Steven/Greg\'s family name'),
    ('S1E44', 'S5E25', Foreshadowing.MAJOR, '"But the records say that gems were wiped out on Earth"; Corrupting light was intended to destroy all Earth gems'),
    ('S1E44', 'S5E27', Foreshadowing.MAJOR, "The Unfamiliar Familiar book; PD's new Pearl (unfamiliar 'familiar')"),
    ('S1E45', 'S3E6', Foreshadowing.MAJOR, "Steven floats cartoonishly; Steven's floating power"),
    ('S1E45', 'S5E18', Foreshadowing.MAJOR, '"If we win, we can never go home"; Rose not an earth Quartz; RQ=PD'),
    ('S1E45', 'S2E20', Foreshadowing.MAJOR, '"My Pearl"; Pearls as servants'),
    ('S1E45', 'S5E18', Foreshadowing.MAJOR, '"My Pearl"; Pearl belonged to Rose'),
    ('S1E46', 'S5E25', Foreshadowing.MAJOR, "Clone Connie matches White Pearl's design"),
    ('S1E48', 'S2E13', Foreshadowing.MINOR, "Vidalia's onion-themed name; Vidalia is Onion's mother"),
    ('S1E51', 'S1E52', Foreshadowing.MAJOR, '"this shameless display" - Jasper, of Garnet; Garnet fusion'),
    ('S1E51', 'S2E21', Foreshadowing.MAJOR, '"a puny overcooked runt" - Jasper, of Amethyst; Amethyst defective'),
    ('S1E52', 'S2E24', Foreshadowing.MAJOR, 'Diamond authority floor symbol; Existence of diamond authority'),
    ('S1E52', 'S3E23', Foreshadowing.MAJOR, 'Diamond authority symbol missing pink; "What you did to [PD]"'),
    ('S2E6', 'S2E24', Foreshadowing.MAJOR, 'Diamond authority symbol in arena; Existence of diamond authority'),
    ('S2E6', 'S3E24', Foreshadowing.MAJOR, 'Cracked PD symbol; shattering of PD'),
    ('S2E7', 'S4E12', Foreshadowing.MAJOR, 'Human zoo mentioned by ronaldo'),
    ('S2E11', 'S5E18', Foreshadowing.MAJOR, "Pink diamond on Sardonyx's feet; Pearl belonged to PD"),
    ('S2E15', 'S2E20', Foreshadowing.MAJOR, '"I\'m just a Pearl"; Pearls as servants'),
    ('S2E17', 'S4E11', Foreshadowing.MAJOR, '"I can\'t help it if I make a scene / stepping out of my hot pink limousine"; PD/palanquin'),
    ('S2E18', 'S4E5', Foreshadowing.MINOR, 'Happy Bear/Sad Bunny; Mr. Smiley/Mr. Frowney'),
    ('S2E20', 'S2E22', Foreshadowing.MINOR, '"Welcome to Earth"'),
    ('S2E20', 'S5E18', Foreshadowing.MAJOR, '"she looks like a fancy one"; Pearl belonged to PD"'),
    ('S2E24', 'S5E12', Foreshadowing.MAJOR, 'Moon base diamond throne is small; PD design'),
    ('S2E24', 'S5E18', Foreshadowing.MAJOR, "PD symbols in Lion's warp; RQ=PD"),
    ('S2E24', 'S5E18', Foreshadowing.MAJOR, '"We are literally walking in the footsteps of the diamonds."; RQ=PD'),
    ('S3E3', 'S3E8', Foreshadowing.MINOR, "Pepe's Burgers ad in background"),
    ('S3E3', 'S3E14', Foreshadowing.MAJOR, 'Yellow/blue/white-tinged nova shown in flashback; Source of corruption'),
    ('S3E3', 'S3E20/21', Foreshadowing.MAJOR, "Bismuth briefly appears in flashback; Bismuth's identity"),
    ('S3E6', 'S5E18', Foreshadowing.MAJOR, "Steven's skull appears on a pink diamond-shaped pillow; RQ=PD"),
    ('S3E8', 'S4E15', Foreshadowing.MAJOR, 'Greg/Pearl yellow/blue symbolism; YD/BD mourning PD'),
    ('S3E16', 'S5E3', Foreshadowing.MAJOR, '"you better pray your space goddess\' magic can bring people back from the dead"'),
    ('S3E20/21', 'S5E18', Foreshadowing.MAJOR, "Rose's sword couldn't shatter gems; PD still alive"),
    ('S3E20/21', 'S5E25', Foreshadowing.MINOR, "Bismuth mentions defeating a Nephrite from a drop-ship; Nephrite's name"),
    ('S3E22', 'S4E15', Foreshadowing.MINOR, "Carnelian and Skinny's exit holes described"),
    ('S3E24', 'S5E6', Foreshadowing.MAJOR, "Pearl covering her mouth when details of PD's death are brought up"),
    ('S3E24', 'S5E18', Foreshadowing.MAJOR, "Eyeball claims to have witnessed RQ murder PD while currently being fooled by shapeshifting; Pearl's role in PD's 'shattering'"),
    ('S3E25', 'S5E18', Foreshadowing.MAJOR, '"That\'s more of a pinkish-red than a real Rose Quartz reddish-pink."; RQ=PD'),
    ('S4E3', 'S4E11', Foreshadowing.MAJOR, "PD's palanquin appears in journal"),
    ('S4E3', 'S5E4', Foreshadowing.MAJOR, "A non-magical lion with the same nose as Lion is seen in the flashback; Lion's origin"),
    ('S4E7', 'S5E18', Foreshadowing.MAJOR, 'Garbanzo fakes his own death; PD faking her death'),
    ('S4E10', 'S5E18', Foreshadowing.MAJOR, "Baby Steven's clothes make diamond shape around his gem; RQ=PD"),
    ('S4E12', 'S5E18', Foreshadowing.MAJOR, '"When I still served... Homeworld"; Pearl unwilling to reveal the gem she served; Pearl belonged to PD'),
    ('S4E17', 'S5E23/24', Foreshadowing.MINOR, "Lonely Arms video game image looks like Cluster/YD's ship arm wresting"),
    ('S4E21', 'S5E18', Foreshadowing.MAJOR, "Pink's ship in desert where Rose stores her stuff; RQ=PD"),
    ('S5E2', 'S5E18', Foreshadowing.MAJOR, '"Someone with supreme authority"; RQ=PD'),
    ('S5E12', 'S5E18', Foreshadowing.MAJOR, "Steven has PD's memories; RQ=PD"),
    ('S5E13', 'S5E18', Foreshadowing.MAJOR, '"Rose Quartz isn\'t real"; RQ=PD'),
    ('S5E20', 'S5E21', Foreshadowing.MINOR, '"Why would she be a cowboy?!"'),
    ('S5E17', 'S5E23/24', Foreshadowing.MINOR, '"You could drop the barn on the beach"'),
    ('S5E25', 'S5E27', Foreshadowing.MAJOR, 'Gem on stomach; White Pearl originally belonged to PD')]
