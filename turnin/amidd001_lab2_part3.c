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
    DDRC = 0xFF; PORTC = 0x00;
    
    unsigned char cntavail;
    unsigned char tmpA;

    /* Insert your solution below */
    while (1) {
	tmpA = PINA & 0xFF; //grabs all bits from PORTA
	if(tmpA == 0x00)
	{
		cntavail = 0x04;
	}
	else if (tmpA == 0x01)
	{
		cntavail = 0x03;
	}
	else if (tmpA == 0x02)
	{
		cntavail = 0x03;
	}
	else if (tmpA == 0x03)
	{
		cntavail = 0x02;
	}
	else if (tmpA == 0x04)
        {
                cntavail = 0x03;
        }
	else if (tmpA == 0x05)
        {
                cntavail = 0x02;
        }
	else if (tmpA == 0x06)
        {
                cntavail = 0x02;
        }
	else if (tmpA == 0x07)
        {
                cntavail = 0x01;
        }
	else if (tmpA == 0x08)
        {
                cntavail = 0x03;
        }
	else if (tmpA == 0x09)
        {
                cntavail = 0x02;
        }
	else if (tmpA == 0x0A)
        {
                cntavail = 0x02;
        }
	else if (tmpA == 0x0B)
        {
                cntavail = 0x01;
        }
	else if (tmpA == 0x0C)
        {
                cntavail = 0x02;
        }
	else if (tmpA == 0x0D)
        {
                cntavail = 0x01;
        }
	else if (tmpA == 0x0E)
        {
                cntavail = 0x01;
        }
	else if (tmpA == 0x0F)
        {
                cntavail = 0x80; //sets available spaces to PC3...PC0, and sets PC7 to 1 because the parking lot is full.
        }
	else
	{
		cntavail = 0x00;
	}
	PORTC = cntavail;
    }
    
    return 0;
}