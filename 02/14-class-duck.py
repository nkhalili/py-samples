class Duck:
    sound = 'Quack quack.'
    movement = 'Walks like a duck.'

    # self references to an object of the class
    def quack(self):
        print(self.sound)

    def move(self):
        print(self.movement)

def main():
    # donal is an object of Duck class
    donald = Duck()
    donald.quack()
    donald.move()

    # you also have access directly to sound itself!
    print(donald.sound)

if __name__ == "__main__":
    main()
