import pickle
import argparse as ap

class Ninja:
    def __init__(self):
        self.days = 0
        self.smash = 0
        self.showdown = 0
        self.climbing = 0
        self.weed = 0
        self.eat_out = 0
        self.cook = 0
        self.bass = 0
        self.workout = 0
        self.yoga = 0
        self.funlearn = 0
        self.meditate = 0
        self.tv = 0
        self.read = 0
        self.reflection = 0
        self.goals = 0
        self.base = 0
        self.stretch = 0
        self.sweets = 0
        
    def add(self, args):
        arg_dict = vars(args)
        self.days += arg_dict['day']
        self.smash += arg_dict['s']
        self.showdown += arg_dict['p']
        self.climbing += arg_dict['c']
        self.weed += arg_dict['w']
        self.eat_out += arg_dict['o']
        self.cook += arg_dict['k']
        self.bass += arg_dict['b']
        self.workout += arg_dict['x']
        self.yoga += arg_dict['y']
        self.funlearn += arg_dict['i']
        self.meditate += arg_dict['m']
        self.tv += arg_dict['t']
        self.read += arg_dict['r']
        self.reflection += arg_dict['f']
        self.goals += arg_dict['g']
        self.base += arg_dict['a']
        self.stretch += arg_dict['z']
        self.sweets += arg_dict['e']
        
    def score(self):
        good = self.stretch + self.goals + self.base + self.reflection + self.read + self.meditate + self.funlearn + self.yoga + self.workout + self.bass + self.cook + self.climbing
        bad = self.smash + self.weed + self.eat_out + self.tv + self.showdown + self.sweets
        return good - bad
        
    def __str__(self):
        return "day: " + str(self.days) + "|" + "smash_hours: " + str(self.smash) + "|showdown_hours: " + str(self.showdown) + "|climbing: " + str(self.climbing) + "|weed: " + str(self.weed) + "|eat_out: " + str(self.eat_out) + "|cook: " + str(self.cook) + "|bass: " + str(self.bass) + "|workouts: " + str(self.workout) + "|yoga: " + str(self.yoga) + "|funlearn: " + str(self.funlearn) + "|meditate: " + str(self.meditate) + "|tv: " + str(self.tv) + "|read: " + str(self.read) + "|reflection: " + str(self.reflection) + "|wrote goals: " + str(self.goals) + "|reached base goals: " + str(self.base) + "|reached stretch goals: " + str(self.stretch) + "|sweets: " + str(self.sweets)
        
        
def get_args():
    p = ap.ArgumentParser()
    p.add_argument("--load", type=str, default="ninja", help="file to load tracker from")
    p.add_argument("--save", type=str, default="ninja")
    p.add_argument("--day", type=int, default = 0)
    p.add_argument("--s", type=int, default=0, help="smash hours")
    p.add_argument("--p", type=int, default=0, help="showdown hours")
    p.add_argument("--c", type=int, default=0, help="days went climbing")
    p.add_argument("--w", type=int, default=0, help="days smoked weed")
    p.add_argument("--o", type=int, default=0, help="meals eaten out")
    p.add_argument("--k", type=int, default=0, help="meals cooked")
    p.add_argument("--b", type=int, default=0, help="played bass")
    p.add_argument("--x", type=int, default=0, help="worked out")
    p.add_argument("--y", type=int, default=0, help="did yoga")
    p.add_argument("--i", type=int, default=0, help="learned something for fun(youtube)")
    p.add_argument("--m", type=int, default=0, help="times meditated")
    p.add_argument("--t", type=int, default=0, help="tv episodes watched")
    p.add_argument("--r", type=int, default=0, help="times read")
    p.add_argument("--f", type=int, default=0, help="wrote weekly reflection")
    p.add_argument("--g", type=int, default=0, help="wrote daily/weekly goals")
    p.add_argument("--a", type=int, default=0, help="completed all base daily/weekly goals")
    p.add_argument("--z", type=int, default=0, help="completed all stretch daily/weekly goals")
    p.add_argument("--e", type=int, default=0, help="sweets eaten")
    return p.parse_args()

def main(args):
    #Want: an easy way to load in arguments, save them in a tracker
    #can use vars to get dict view of arguments
    cur_ninja = pickle.load(open(args.load, 'rb'))
#    cur_ninja = Ninja()
    cur_ninja.add(args)
    print(cur_ninja)
    print(cur_ninja.score())
    pickle.dump(cur_ninja, open(args.save, 'wb'))

if __name__ == "__main__":
    args = get_args()
    main(args)
