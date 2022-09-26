def FUN_writing(adj,verb1,verb2,celebrity):
    print(f"In this {adj} story the main protagonist is a lot like you. The warm-hearted young man would {verb1} hard every day and search for better ways to improve the situation. The reality can be hard sometimes; the things can always {verb2} as time goes by. It is just as bright as what {celebrity} looks")

def FACT_writing(noun,another_noun,verb,adv):
    print(f"A show {noun} is a commitment of focus to the audience. It tells the creators and audience alike what the {another_noun} is, and more importantly, what the {another_noun} is not. A {noun} keeps content on track. The audience will {verb} and continue to {verb} as time goes by. The {adv} solution start to dominate the {noun} and lead every party in the future.")
style = input("Are you looking for FUN or FACT?").upper()
FUN = 'FUN'
FACT= 'FACT'
if style ==FUN:
    adj =  input("Enter an 'adj' such as cool:")
    verb1 = input("Enter a 'Verb' such as make:")
    verb2 = input("Enter a 'Verb' such as enter:")
    celebrity = input("Enter a 'Name' such as James Bond:")
    FUN_writing(adj,verb1,verb2,celebrity)

if style == FACT:    
    noun =  input("Enter a 'noun' such as Playbook:")
    another_noun = input("Enter a 'noun' such as notion:")
    verb = input("Enter a 'Verb' such as rise:")
    adv = input("Enter a 'Adverb' such as lovely:")
    FACT_writing(noun,another_noun,verb,adv)