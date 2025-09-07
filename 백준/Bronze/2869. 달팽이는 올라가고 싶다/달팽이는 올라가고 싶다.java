import java.util.Scanner;

public class Main
{
	public static void main(String[] args) {
		double a,b,c;
		Scanner sc = new Scanner(System.in);
		
		a = sc.nextDouble();
		b = sc.nextDouble();
		c = sc.nextDouble();
		int d = (int)Math.ceil((c-a)/(a-b));
        System.out.println(d+1);
	}
}
