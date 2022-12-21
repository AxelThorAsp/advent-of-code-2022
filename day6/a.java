
import java.io.FileReader;
import java.io.PrintStream;

public class a {

    public static void main(String[] args) throws Exception{

        int counter[] = new int[26];

        PrintStream o = System.out;
        String filepath = args[0];
        
        FileReader fr = new FileReader(filepath);
        
        char buffer[] = new char[4096];

        int n = fr.read(buffer);
        fr.close();
        int l,r;
        l = 0;
        r = 4;
        int inc = 4;
        for (int i = 0; i < 4; i++) {
            counter[buffer[i] - 'a'] += 1;
        }

        while (r < n) {
            for (int i = l; l < r; i++) {
                if (counter[buffer[i] - 'a'] != 1) {
                    break;
                }
                if (i == r - 1) {
                    o.println(inc);
                    return;
                }
            }
            inc++;
            counter[buffer[l++] - 'a'] -= 1;
            counter[buffer[r++] - 'a'] += 1;
        }
    }
}