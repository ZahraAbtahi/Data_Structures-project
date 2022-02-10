//@author Sonia Abtahi
import java.util.*;
import javax.swing.*;
public class YasQueue1 // my public class whish has a main and a inner class to implement Yas's Queue Using two Stacks . 
{  
    static Stack < Integer > stack1 = new Stack < Integer >();  
    static Stack < Integer > stack2 = new Stack < Integer >(); 
    public void Enqueue(int student_number) // this void method will push all student numbers in the stack1 .
    { 
        stack1.push(student_number); 
    } 
    public int Dequeue() // this int method without input argumant will push all student numbers from stack1 to stack2 to inverse stack1 . 
    { 
        if(stack1.size() == 0) 
        { 
            if(stack2.size() == 0) 
            { 
                System.out.println(" The Yas's Queue is empty ! "); 
                return -1; 
            } 
        } 
        while(stack1.size() > 0) 
        { 
            stack2.push(stack1.pop()); 
        } 
        return stack2.pop(); 
    } 
    public static void main(String[] args) // main method to run program .
    { 
        YasQueue1 Yas = new YasQueue1();
        String lenght0 = JOptionPane.showInputDialog(" Please enter your Queue's lenght : ");
        int lenght = Integer.parseInt(lenght0);
        if(lenght != 0)
        { 
            for(int i = 0 ; i < lenght ; i++) 
            { 
                String student_number0 = JOptionPane.showInputDialog(" Please enter your student number :");
                int student_number = Integer.parseInt(student_number0);
                Yas.Enqueue(student_number);  
            } 
            JOptionPane.showMessageDialog(null , " The Queue will be like : ");  
            for(int i = 0 ; i < lenght ; i++) 
            { 
                JOptionPane.showMessageDialog(null,Yas.Dequeue()); 
            }
        }
        else 
            JOptionPane.showMessageDialog(null , " You can't have a queue in Yas Restaurant ! "); 
    }
}
// code without javax.swing .
/*Scanner Input = new Scanner(System.in);
        YasQueue Yas = new YasQueue();
        System.out.println(" Please enter your Queue's lenght : ");
        int lenght = Input.nextInt();
        if(lenght != 0)
        { 
            for(int i = 0 ; i < lenght ; i++) 
            { 
                System.out.print(" Please enter your student number : "); 
                int student_number = Input.nextInt(); 
                Yas.Enqueue(student_number);  
                System.out.println("--------------------");
            } 
            System.out.println(" The Queue will be like : "); 
            for(int i = 0 ; i < lenght ; i++) 
            { 
                System.out.println(Yas.Dequeue()); 
                System.out.println("----------------------"); 
            }
        }
        else
            System.out.println("\n----------------------\n");
            System.out.println("\nYou can't have a queue in the Yas ! \n");
    }
}
*/


