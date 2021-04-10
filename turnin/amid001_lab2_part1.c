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
    DDRB = 0xFF; PORTB = 0x00;

    unsigned char tmpA;
    unsigned char tmpB;

    /* Insert your solution below */
    while (1) {
	tmpA = PINA & 0xFF; //grabs all bits from PORTA
	if(tmpA == 0x03) // tmpA == 0x03
	{
		tmpB = 0x00;;
	}
	else if (tmpA == 0x02) //tmpA == 0x02
	{
		tmpB = 0x00;
	}
	else if (tmpA == 0x01) //tmpA == 0x01
	{
		tmpB = 0x01;
	}
	else if (tmpA == 0x00) //tmpA == 0x00
	{
		tmpB = 0x00;
	}
	else
	{
		tmpB = 0x00;
	}
	PORTB = tmpB;
    }
    
    return 0;
}
