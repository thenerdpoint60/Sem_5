import java.util.*;
class MonoalphabeticCipher
{
	char[] plain={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
	char[] cipher ={'Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M'};
	char[] encrypted =new char[20];
	public String doEncryption(String a)
	{
		char[] c = new char[a.length()];
		for(int i=0;i<a.length();i++)
		{
			for(int j=0;j<plain.length;j++)
			{
				if(a.charAt(i)==plain[j])
				{
					c[i]=cipher[j];
					
				}
			}
		}
		String cipherText= new String(c);
		return cipherText;
		
		
	}
	public String doDecryption(String c)
	{
		char[] p = new char[c.length()];
		for (int i=0;i<c.length();i++)
		{
			for(int j=0;j<cipher.length;j++)
			{
				if(c.charAt(i)==cipher[j])
				{
					p[i]=plain[j];
					
				}
			}
		}
		String pt=new String(p);
		return pt;
	}
	
	
	public static void main(String[] args)
	{
		MonoalphabeticCipher mc = new MonoalphabeticCipher();
		System.out.println("Enter plainText:");
		Scanner sc = new Scanner(System.in);
		String m=sc.next();
		String c = mc.doEncryption(m);
		System.out.println("Cipher text"+c);
		String p = mc.doDecryption(c);
		System.out.println("Plain Text"+p);
	}
	
	
	
}