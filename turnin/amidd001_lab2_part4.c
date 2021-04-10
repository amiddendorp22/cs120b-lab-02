/*	Author: amidd001
 *  Partner(s) Name: Jo Smith
 *	Lab Section:
 *	Assignment: Lab #  Exercise #
 *	Exercise Description: [optional - include for your own benefit]
 *
 *	I acknowledge all content contained herein, excluding template or example
 *	code, is my own original work.
 */
#include <avr/io.h>
#ifdef _SIMULATE_
#include "simAVRHeader.h"
#endif

int main(void) {
    /* Insert DDR and PORT initializations */
    DDRA = 0x00; PORTA = 0xFF;
    DDRB = 0x00; PORTB = 0xFF;
    DDRC = 0x00; PORTC = 0xFF;
    DDRD = 0xFF; PORTD = 0x00;
    
    unsigned char tmpA;
    unsigned char tmpB;
    unsigned char tmpC;
    unsigned char tmpD;
    unsigned char maxWeight;
    unsigned char currWeight;

    /* Insert your solution below */
    while (1) {
	tmpA = PINA & 0xFF; //grabs all bits from PORTA
	tmpB = PINB & 0xFF; //grabs all bits from PORTB
	tmpC = PINC & 0xFF; //grabs all bits from PORTC

	maxWeight = 0x8C; //defines the max weight for the car in hexadecimal. (140 kg)
	currWeight = tmpA + tmpB + tmpC; //holds the current weight of the whole cart.

	//max weight able to approx. on pins PD7..PD2 is 0xFC (252kg). We will ignore bits PD1,PD0. This keeps the most significant bits.
	// If the total cart's weight is under 4kg (unlikely), PD7..PD2 = 000000
	//If the cart's total passenger weight > 140kg (0x8C), then PD0 = 1
	//If the difference between tmpA and tmpC > 80kg (0x50), then PD1 = 1
	
	if(currWeight > maxWeight)
	{
		if(tmpA > tmpC)
		{
			if( (tmpA - tmpC) > 0x50)
			{
				// we want FFFFFF11
				tmpD = currWeight & 0xFC; //makes D7..D2 = currWeight7..currWeight2
				tmpD = tmpD + 0x03; //sets D1 and D0 to 1
			}
			else
			{
				// we want FFFFFF01
				tmpD = currWeight & 0xFC; //makes D7..D2 = currWeight7..currWeight2
				tmpD = tmpD + 0x01; //makes D0 = 1
			}
		}
		else
		{
			if( (tmpC - tmpA) > 0x50)
			{
				//we want FFFFFF11
				tmpD = currWeight & 0xFC; //makes D7..D2 = currWeight7..currWeight2
				tmpD = tmpD + 0x03; //sets D1 and D0 to 1
			}
			else
			{
				//we want FFFFFF01
				tmpD = currWeight & 0xFC; //makes D7..D2 = currWeight7..currWeight2
				tmpD = tmpD + 0x01; //makes D0 = 1
			}
		}
	}
	else
	{
		if(tmpA > tmpC)
		{
			if( (tmpA - tmpC) > 0x50)
			{
				// we want FFFFFF10
				tmpD = currWeight & 0xFC; //makes D7..D2 = currWeight7..currWeight2
				tmpD = tmpD + 0x02; //sets D1 to 1
			}
			else
			{
				// we want FFFFFF00
				tmpD = currWeight & 0xFC; //makes D7..D2 = currWeight7..currWeight2
			}
		}
		else
		{
			if( (tmpC - tmpA) > 0x50)
			{
				//we want FFFFFF10
				tmpD = currWeight & 0xFC; //makes D7..D2 = currWeight7..currWeight2
				tmpD = tmpD + 0x02;
			}
			else
			{
				//we want FFFFFF00
				tmpD = currWeight & 0xFC;
			}
		}
    	} //end of else
	PORTD = tmpD;
    
} //end of while
return 0;
}// end of main
