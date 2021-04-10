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
tests = [ {'description': 'PINA PINB PINC  == 0x32 0x32 0x32 (50 kg each, overweight, balanced)',
    'steps': [ {'inputs': [('PINA',0x32), ('PINB', 0x32), ('PINC', 0x32)], 'iterations': 5 } ],
    'expected': [('PORTD',0x95)],
    },
    {'description': 'PINA PINB PINC == 0x64 0x32 0x01 (overweight, unbalanced)',
    'steps': [ {'inputs': [('PINA', 0x64), ('PINB', 0x32), ('PINC', 0x01)], 'iterations': 5 } ],
    'expected': [('PORTD', 0x97)],
    },
    {'description': 'PINA PINB PINC == 0x14 0x14 0x14 (20kg each, underweight, balanced) ',
    'steps': [ {'inputs': [('PINA', 0x14), ('PINB', 0x14), ('PINC', 0x14)], 'iterations': 5 } ],
    'expected': [('PORTD', 0x3C)],
    },
    {'description': 'PINA PINB PINC == 0x01 0x1E 0x52 (underweight, not balanced)',
     'steps': [ {'inputs': [('PINA', 0x01), ('PINB', 0x1E), ('PINC', 0x52)], 'iterations': 5} ],
     'expected': [('PORTD', 0x72)],
    },
    {'description': 'PINA PINB PINC = 0xFF 0xFF 0xFF (overweight, balanced, edge case)',
     'steps': [ {'inputs': [('PINA', 0xFF), ('PINB', 0xFF), ('PINC', 0xFF)], 'iterations': 5} ],
     'expected': [('PORTD', 0xFD)],
    },
    {'description': 'PINA PINB PINC = 0x00 0x00 0x00 (underweight, balanced, edge case)',
     'steps': [ {'inputs': [('PINA', 0x00), ('PINB', 0x00), ('PINC', 0x00)], 'iterations': 5} ],
     'expected': [('PORTD', 0x00)],
    },
    ]
#watch = ['PORTB']

