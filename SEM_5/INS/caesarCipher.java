import java.util.*;

public class casarCipher
{
	public static void main(String args[])
	{
		int i;
		System.out.println("Enter a text");
		Scanner sc = new Scanner(System.in);
		String str1=sc.nextLine();
		String str2= str1.trime();
		String str= str2.replaceAll("\\s+","");
		System.out.println(""+str);
		for(i=0;i<str.length();i++)
		{
			System.out.println(str.charAt(i)+"\t"+(int)(str.charAt(i)+"\t"+(int)(str.charAt(i)+3)-97%26)+"\t"+(char)((((str.charAt(i)+3)-97)%26)+97));
			
			
		}
		System.out.println("Cipher Text :");
		for(i=0;i<str.length();i++)
		{
			System.out.println((char)((((str.charAt(i)+3)-97)%26)+97));
		}
	}
	
}