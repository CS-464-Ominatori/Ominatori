import javax.imageio.ImageIO;
import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;

public class Main {

    public static void main(String[] args) {

        JFrame frame = new JFrame();

        frame.setPreferredSize(new Dimension(500,700));

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.getContentPane().add(new ImagePanel());
        frame.pack();
        frame.setVisible(true);

    }
}
