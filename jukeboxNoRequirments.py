def run():
    userIn = input('Select a song. >>')
    if userIn in ['big iron', 'e1m1', 'ichidaiji', 'moonlight',  'telecaster stripes']:
        print(f'Playing {userIn}')
    else:
        import random
        print(f"We could't find that song, playing {random.choice(['big iron', 'e1m1', 'ichidaiji', 'moonlight',  'telecaster stripes'])} instead.")
run()