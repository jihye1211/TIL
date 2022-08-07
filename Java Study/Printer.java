import java.util.Scanner;

public class Printer {
    public static void main(String computePrintJob[]) {
     
      String paperSize="";
      String colorType="";
      int count = 0;
      
      Scanner sc = new Scanner(System.in);

      System.out.print("Enter print job info: ");
      paperSize = sc.next();
      colorType = sc.next();
      count = sc.nextInt();
      
      if(colorType.equals("Grayscale"))
      {
    	  colorType = "5";
      } else if(colorType.equals("Color"))
      {
    	  colorType = "25";
      }
      
      switch(paperSize) {
      case "A4": paperSize = "40";
           break;
      case "A5": paperSize = "10";
           break;
      case "Letter": paperSize = "45";
           break;
      case "Legal": paperSize = "30";
           break;
      default: 
          System.out.println("Please enter the paperSize one of A4, A5, Letter, Legal.");
           break;
}
         
     int totalCost = (Integer.parseInt(paperSize)+Integer.parseInt(colorType))*count;
     
     if(totalCost%10 != 0)
     {
         totalCost = totalCost+5;
     }
     
     System.out.println("Print job cost: "+totalCost);
      
    }
}