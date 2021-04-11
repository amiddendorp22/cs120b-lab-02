# Array of tests to run (in order)
# Each test contains
#   description - 
#   steps - A list of steps to perform, each step can have
#       inputs - A list of tuples for the inputs to apply at that step
#       *time - The time (in ms) to wait before continuing to the next step 
#           and before checking expected values for this step. The time should be a multiple of
#           the period of the system
#       *iterations - The number of clock ticks to wait (periods)
#       expected - The expected value at the end of this step (after the "time" has elapsed.) 
#           If this value is incorrect the test will fail early before completing.
#       * only one of these should be used
#   expected - The expected output (as a list of tuples) at the end of this test
# An example set of tests is shown below. It is important to note that these tests are not "unit tests" in 
# that they are not ran in isolation but in the order shown and the state of the device is not reset or 
# altered in between executions (unless preconditions are used).
tests = [ {'description': 'PA0 PA1 PA2 PA3  == 0 0 0 0',
    'steps': [ {'inputs': [('PINA',0x00)], 'iterations': 5 } ],
    'expected': [('PORTC',0x04)],
    },
    {'description': 'PA0 PA1 PA2 PA3  == 0 0 0 1',
    'steps': [ {'inputs': [('PINA', 0x01)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x03)],
    },
    {'description': 'PA0 PA1 PA2 PA3  == 0 0 1 0',
    'steps': [ {'inputs': [('PINA', 0x02)], 'iterations': 5 } ],
    'expected': [('PORTC', 0x03)],
    },
    {'description': 'PA0 PA1 PA2 PA3  == 0 0 1 1',
     'steps': [ {'inputs': [('PINA', 0x03)], 'iterations': 5} ],
     'expected': [('PORTC', 0x02)],
    },
    {'description': 'PA0 PA1 PA2 PA3  == 0 1 0 0',
     'steps': [ {'inputs': [('PINA', 0x04)], 'iterations': 5} ],
     'expected': [('PORTC', 0x03)],
    },
    {'description': 'PA0 PA1 PA2 PA3  == 0 1 0 1',
     'steps': [ {'inputs': [('PINA', 0x05)], 'iterations': 5} ],
     'expected': [('PORTC', 0x02)],
    },
    {'description': 'PA0 PA1 PA2 PA3  == 0 1 1 0',
     'steps': [ {'inputs': [('PINA', 0x06)], 'iterations': 5} ],
     'expected': [('PORTC', 0x02)],
    },
    {'description': 'PA0 PA1 PA2 PA3  ==0 1 1 1',
     'steps': [ {'inputs': [('PINA', 0x07)], 'iterations': 5} ],
     'expected': [('PORTC', 0x01)],
    },
    {'description': 'PA0 PA1 PA2 PA3  == 1 0 0 0',
     'steps': [ {'inputs': [('PINA', 0x08)], 'iterations': 5} ],
     'expected': [('PORTC', 0x03)],
    },
    {'description': 'PA0 PA1 PA2 PA3  == 1 0 0 1',
     'steps': [ {'inputs': [('PINA', 0x09)], 'iterations': 5} ],
     'expected': [('PORTC', 0x02)],
    },
    {'description': 'PA0 PA1 PA2 PA3  == 1 0 1 0',
     'steps': [ {'inputs': [('PINA', 0x0A)], 'iterations': 5} ],
     'expected': [('PORTC', 0x02)],
    },
    {'description': 'PA0 PA1 PA2 PA3  == 1 0 1 1',
     'steps': [ {'inputs': [('PINA', 0x0B)], 'iterations': 5} ],
     'expected': [('PORTC', 0x01)],
    },
    {'description': 'PA0 PA1 PA2 PA3  == 1 1 0 0',
     'steps': [ {'inputs': [('PINA', 0x0C)], 'iterations': 5} ],
     'expected': [('PORTC', 0x02)],
    },
    {'description': 'PA0 PA1 PA2 PA3  == 1 1 0 1',
     'steps': [ {'inputs': [('PINA', 0x0D)], 'iterations': 5} ],
     'expected': [('PORTC', 0x01)],
    },
    {'description': 'PA0 PA1 PA2 PA3  == 1 1 1 0',
     'steps': [ {'inputs': [('PINA', 0x0E)], 'iterations': 5} ],
     'expected': [('PORTC', 0x01)],
    },
    {'description': 'PA0 PA1 PA2 PA3 == 1 1 1 1',
     'steps': [ {'inputs': [('PINA', 0x0F)], 'iterations': 5} ],
     'expected': [('PORTC', 0x80)],
    },
    {'description': 'PINA: 0x80 => PORTC: 4',
     'steps': [ {'inputs': [('PINA',0x80)], 'iterations': 5} ],
     'expected': [('PORTC', 0x04)],
    },
    {'description': 'PINA: 0x4F => PORTC[3:0]: 0, PC7: 1',
     'steps': [ {'inputs': [('PINA', 0x4F)], 'iterations': 5} ],
     'expected': [('PORTC', 0x80)],
    },
    ]
#watch = ['PORTB']

