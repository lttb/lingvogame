import re

import IO
import analyzer
import suggest


def create(data, ** options):
    initialScore = {'user': 0, 'game': 0}

    def start(score):
        initialHealth = 4
        initialWord, bigrams = analyzer.build(data, ** options)

        IO.OUT('\n' + 'New round!' + '\n')
        IO.OUT('Score: user - %(user)s, game - %(game)s' % score + '\n')

        def step(tips, health):
            currentScore = {}

            IO.OUT('You have %(health)s %(attempt)s' % {
                'health': health,
                'attempt': 'attempts' if health > 1 else 'attempt'
            })

            IO.OUT(re.sub(
                r'\b%s\b' % initialWord,
                '_' * len(initialWord),
                tips[0]
            ))

            word = input('> ')

            if word == initialWord:
                currentScore['user'] = score['user'] + 1
                IO.OUT('You win!')
            elif health == 1:
                currentScore['game'] = score['game'] + 1
                IO.OUT('Sorry, you lose :(')
            else:
                return step(tips[1:], health - 1)

            return start({**score, **currentScore})

        step(bigrams + suggest.get(initialWord), initialHealth)

    start(initialScore)
