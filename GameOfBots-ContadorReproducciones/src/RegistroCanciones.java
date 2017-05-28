import java.util.Scanner;

public class RegistroCanciones {

	public static void main(String[] args) {
		Cancion[] cancion = new Cancion[13];
		cancion[0] = new Cancion("The Chainsmokers", "Paris");
		cancion[1] = new Cancion("The Beatles", "Yesterday - Remastered");
		cancion[2] = new Cancion("Green Day", "Basket Case");
		cancion[3] = new Cancion("Harry Styles", "Sign of the Times");
		cancion[4] = new Cancion("Ben E. King", "Stand By Me");
		cancion[5] = new Cancion("Bruno Mars", "Just the Way You Are");
		cancion[6] = new Cancion("Coldplay", "Speed Of Sound");
		cancion[7] = new Cancion("Red Hot Chili Peppers", "Otherside");
		cancion[8] = new Cancion("The Beatles", "Penny Lane - Remastered 2015");
		cancion[9] = new Cancion("Lukas Graham", "7 Years");
		cancion[10] = new Cancion("Simple Plan", "Welcome To My Life");
		cancion[11] = new Cancion("Galantis", "No Money");
		cancion[12] = new Cancion("Passenger", "Let Her Go");
		int opcion = 0;
		do {
			Scanner sc = new Scanner(System.in);
			opcion = sc.nextInt();
			switch (opcion) {
			case 1:
				cancion[0].reproduccion();
				break;
			case 2:
				cancion[1].reproduccion();
				break;
			case 3:
				cancion[2].reproduccion();
				break;
			case 4:
				cancion[3].reproduccion();
				break;
			case 5:
				cancion[4].reproduccion();
				break;
			case 6:
				cancion[5].reproduccion();
				break;
			case 7:
				cancion[6].reproduccion();
				break;
			case 8:
				cancion[7].reproduccion();
				break;
			case 9:
				cancion[8].reproduccion();
				break;
			case 10:
				cancion[9].reproduccion();
				break;
			case 11:
				cancion[10].reproduccion();
				break;
			case 12:
				cancion[11].reproduccion();
				break;
			case 13:
				cancion[12].reproduccion();
				break;
			default:
				break;
			}
		} while (opcion != 0);
		for (int i = 0; i < 9; i++) {
			System.out.println(cancion[i].toString());
		}
	}

}
