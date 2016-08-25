import java.io.*;
public class Main {
    public static void main (String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        while ((line = buffer.readLine()) != null) {
            line = line.trim();
           String [] lineas = line.split(",");
           int s1 = Integer.parseInt(lineas[0]);
           int s2 = Integer.parseInt(lineas[1]);
           System.out.println(multiploMenor(s1,s2));
        }
    }
    
    public static int multiploMenor (int s1,int s2){
        int multiplo = s2; 
        while (multiplo < s1)
            {
            multiplo+= s2;
         }
        return multiplo;
    }
}
 