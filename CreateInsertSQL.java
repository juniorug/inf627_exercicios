
import java.util.Random;
import java.lang.Math;

public class CreateInsertSQL {

    public static void main(String[] args) {
        int minutes = 0;
        int hours = 8;
        System.out.println("INSERT INTO dashboard_sensormeasurement (sensor_id,value, datetime_measurement) VALUES");
        for (int i = 0; i < 100; i++) {
            
            Random gerador = new Random();
            int numero = gerador.nextInt(40 - 18) + 18;
             
            System.out.println("(1, '"+ numero +"', '"+ manipulateDate(hours, minutes) +"'),");
            minutes += 5;
            if (minutes == 60) {
                minutes = 0;
                hours ++;            
            }
        }

        minutes = 0;
        hours = 8;
        System.out.println("INSERT INTO dashboard_sensormeasurement (sensor_id,value, datetime_measurement) VALUES"); 
        for (int i = 0; i < 100; i++) {
            
            Random gerador = new Random();
            int numero = gerador.nextInt(70 - 40) + 40;
             
            System.out.println("(2, '"+ numero +"', '"+ manipulateDate(hours, minutes) +"'),");
            minutes += 5;
            if (minutes == 60) {
                minutes = 0;
                hours ++;            
            }
        }
        
        minutes = 0;
        hours = 8;
        int numero = 50;
        System.out.println("INSERT INTO dashboard_sensormeasurement (sensor_id,value, datetime_measurement) VALUES"); 
        for (int i = 0; i < 100; i++) {
                         
            System.out.println("(3, '"+ numero +"', '"+ manipulateDate(hours, minutes) +"'),");
            minutes += 5;
            numero += 5;  
            if (minutes == 60) {
                minutes = 0;
                hours ++;            
            }
        }

    }

    private static String manipulateDate(int hours, int minutes){
        String sb = "2016-04-04 YY:XX:00";
        int length = (int) Math.log10(minutes) + 1;
        String m = "";
        String h = "";
        if (length <= 1){
            m = "0".concat(Integer.toString(minutes));
        } else {
            m = Integer.toString(minutes);
        } 
        length = (int) Math.log10(hours) + 1;
        if (length <= 1){
            h = "0".concat(Integer.toString(hours));
        } else {
            h = Integer.toString(hours);
        }   
        sb = sb.replace("XX", m);
        sb = sb.replace("YY", h);
        return sb;
    }

}


/* '2016-04-04 08:00:00'*/
