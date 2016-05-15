package net.bethydiakabana.project.numbers;

public class BinaryToDecimalConverter {
	public static String decimalToBinary(int integer) {
		return Integer.toBinaryString(integer);
	} // end method convertToBinary
	
	public static int binaryToDecimal(String binaryString) {
		return Integer.parseInt(binaryString, 2);
	} // end method 
}
