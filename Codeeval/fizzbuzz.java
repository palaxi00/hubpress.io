
import java.io.*;
public class Main {
    public static void main (String[] args) throws IOException {
        File file = new File(args[0]);
        BufferedReader buffer = new BufferedReader(new FileReader(file));
        String line;
        while ((line = buffer.readLine()) != null) {
        String[] params = line.split(" ");
		 int a = Integer.parseInt(params[0]);
		 int b = Integer.parseInt(params[1]);
		 int n = Integer.parseInt(params[2]);
		 printFizzBuzz(a, b, n);
		 System.out.println();
        }
    }
    
		private static void printFizzBuzz (int a , int b , int n){
			
			for (int i = 1; i <= n;  i++){
				String salida = "";
    			    	if((i % a==0) && (i %b==0)){
    			    	    salida = "FB";
    			    	}else if(i % a==0) {
        				    salida = "F";
    			    	}else if(i % b==0) {
        				    salida = "B";}else{
        				   salida = String.valueOf(i);
    			    	            }
    				        System.out.print(salida + " ");
			        }
	    	}
    
}
