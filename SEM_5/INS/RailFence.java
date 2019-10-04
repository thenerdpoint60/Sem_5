import java.util.*;
class RailFence
{
	public static void main(String[] args)
	{
		String pt;
		int i;
		System.out.println("Enter Plain text");
		Scanner sc= new Scanner(System.in);
		pt= sc.nextLine();
		char text[] = new char[pt.length()];
		char text1[] = new char[pt.length()];
		for(i=0;i<pt.length();i++)
		{
			if(i%2==0)
			{
				text[i]=pt.charAt(i);
			}
			else
			{
				text1[i]=pt.charAt(i);
			}
		}
		for(i=0;i<pt.length();i++)
		{
			System.out.println(text[i]);
		}
		for(i=0;i<pt.length();i++)
		{
			System.out.println(text1[i]);
		}
	}
}