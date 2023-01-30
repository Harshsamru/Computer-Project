while True:
    print('Press 1 for Akinator')
    print('Press 2 for Guess the number')
    ch = int(input('enter your choice:'))
    if ch == 1:
        while True:
            print('Press 1 for Sports personalities')
            print('Press 2 for Famous personalities of Indian Cinema')
            print('Press 0 to return back to home page')
            l=int(input('Enter your choice'))
            if l==0:
                break
            if l==1:
                import random
                V = random.randrange(0,10)
                T = (('LIONEL MESSI','MESSI',),('YUVRAJ SINGH','YUVRAJ'),('hello'),('hello'),('hello'),('hello'),('hello'),('hello'),('hello'),('hello'))
                L = [{1: "The referred person's father,Jorge, was a steelworker and coach of the local youth football team",
                      2: "This person had growth hormone deficiency, which was stopping his/her normal growth rate at a tender age of 11. "
                       "Most importantly, his/her parents couldn’t afford his treatment of $900 per month",
                      3: "Holds the record for winning the most number of Ballon d'Or awards"},
                      {1:"He/she has won 7 Player of the Series awards in ODI cricket, which is joint 3rd highest by an Indian",
                      2:"The person referred here was diagnosed with a cancerous tumor in his/her left lung and underwent "
                      "chemotherapy treatment in Boston and Indianapolis",
                      3:"On September 19, 2007, at Kingsmead, he/she smashed six sixes in a single over"},
                      {1:'hell0',2:'insert',3:'paste'},
                      {1:'hell0',2:'insert',3:'paste'},
                      {1: 'hell0', 2: 'insert', 3: 'paste'},
                      {1: 'hell0', 2: 'insert', 3: 'paste'},
                      {1: 'hell0', 2: 'insert', 3: 'paste'},
                      {1: 'hell0', 2: 'insert', 3: 'paste'},
                      {1: 'hell0', 2: 'insert', 3: 'paste'},
                      {1: 'hell0', 2: 'insert', 3: 'paste'}]


                for i in range(1,4):
                    print(L[V][i])
                    if i == 3:
                        r = input('enter your answer:')
                    else:
                        r = input('enter your answer or enter N for the next clue:')
                        if r.upper() == 'N':
                            continue
                    if r.upper() in T[V]:
                        print('you entered the correct answer')
                        print('No of clues taken:', i)
                        break
                    else:
                        print('wrong answer')
                        print('The person referred here was', T[V][0])
                        break

            if l==2:
                while True:
                    print('Press 1 for Bollywood-Hindi')#10
                    print('Press 2 for Mollywood-Malayalam')#10
                    print('Press 3 for Sandalwood-Kannada')#10
                    print('Press 4 for Kollywood-Tamil')#10
                    print('Press 5 for Tollywood-Telugu')
                    x = int(input('enter your choice:'))
                    if x == 1:
                        import random
                        V = random.randrange(0, 10)
                        T = (('hello'), ('hello'), ('hello'), ('hello'), ('hello'),
                        ('hello'), ('hello'), ('hello'), ('hello'), ('hello'))
                        L = [{1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'}]

                        for i in range(1, 4):
                            print(list[V][i])
                            if i == 3:
                                r = input('enter your answer:')
                            else:
                                r = input('enter your answer or enter N for the next clue:')
                                if r.upper() == 'N':
                                    continue
                            if r.upper() in T[V]:
                                print('you entered the correct answer')
                                print('No of clues taken:', i)
                                break
                            else:
                                print('wrong answer')
                                print('The person referred here was', T[V][0])
                                break

                    if x == 2:
                        import random
                        V = random.randrange(0, 10)
                        T = (("MOHANLAL","MOHANLAL VISWANATHAN","LALETTAN"),("DULQUER SALMAN","DQ","DULQUER" ), ("FAHADH FAZIL","FAHADH","FAFA"), ('hello'), ('hello'),
                                 ('hello'), ('hello'), ('hello'), ('hello'), ('hello'))
                        L = [{1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'}]

                        for i in range(1, 4):
                            print(L[V][i])
                            if i == 3:
                                r = input('enter your answer:')
                            else:
                                r = input('enter your answer or enter N for the next clue:')
                                if r.upper() == 'N':
                                    continue
                            if r.upper() in T[V]:
                                print('you entered the correct answer')
                                print('No of clues taken:', i)
                                break
                            else:
                                print('wrong answer')
                                print('The person referred here was', T[V][0])
                                break

                    if x == 3:
                        import random
                        V = random.randrange(0, 10)
                        T = (('hello'), ('hello'), ('hello'), ('hello'), ('hello'),
                        ('hello'), ('hello'), ('hello'), ('hello'), ('hello'))
                        L = [{1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'}]

                        for i in range(1, 4):
                            print(L[V][i])
                            if i == 3:
                                r = input('enter your answer:')
                            else:
                                r = input('enter your answer or enter N for the next clue:')
                                if r.upper() == 'N':
                                    continue
                            if r.upper() in T[V]:
                                print('you entered the correct answer')
                                print('No of clues taken:', i)
                                break
                            else:
                                print('wrong answer')
                                print('The person referred here was', T[V][0])
                                break

                    if x == 4:
                        import random
                        V = random.randrange(0, 10)
                        T = (('hello'), ('hello'), ('hello'), ('hello'), ('hello'),
                        ('hello'), ('hello'), ('hello'), ('hello'), ('hello'))
                        L = [{1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'}]

                        for i in range(1, 4):
                            print(L[V][i])
                            if i == 3:
                                r = input('enter your answer:')
                            else:
                                r = input('enter your answer or enter N for the next clue:')
                                if r.upper() == 'N':
                                    continue
                            if r.upper() in T[V]:
                                print('you entered the correct answer')
                                print('No of clues taken:', i)
                                break
                            else:
                                print('wrong answer')
                                print('The person referred here was', T[V][0])
                                break

                    if x == 5:
                        import random
                        V = random.randrange(0, 10)
                        T = (('hello'), ('hello'), ('hello'), ('hello'), ('hello'),
                        ('hello'), ('hello'), ('hello'), ('hello'), ('hello'))
                        L = [{1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'},
                             {1: 'hell0', 2: 'insert', 3: 'paste'}]

                        for i in range(1, 4):
                            print(L[V][i])
                            if i == 3:
                                r = input('enter your answer:')
                            else:
                                r = input('enter your answer or enter N for the next clue:')
                                if r.upper() == 'N':
                                    continue
                            if r.upper() in T[V]:
                                print('you entered the correct answer')
                                print('No of clues taken:', i)
                                break
                            else:
                                print('wrong answer')
                                print('The person referred here was', T[V][0])
                                break

    if ch == 2:
        print('You have only 7 chances to guess the integer between 0 and 100')
        import random
        v = random.randrange(0, 101, 1)
        for i in range(7):
            x = int(input('Enter the num:'))
            if x > v:
                print('Entered number is greater than the random number')1
            elif x < v:
                print('Entered number is lesser than the random number')
            elif x == v:
                print('congrats, you guessed it!!')
                print('No of Guesses:', i+1)
                break
        if x != v:
            print('Game over')
            print('The number was', v)
