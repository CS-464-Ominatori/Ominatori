import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.image.BufferedImage;
import java.beans.PropertyChangeListener;
import java.io.File;
import java.io.IOException;
import java.io.PrintWriter;
import javax.imageio.ImageIO;
import javax.swing.*;

public class ImagePanel extends JPanel{

    private BufferedImage image;
    private String currentImage;
    JCheckBox [] boxes;

    private File files[];
    private int index = 0;
    String [] list = {"Action", "Adventure", "Animation", "Comedy","Crime","Documentary",
            "Drama", "Family", "Fantasy", "History", "Horror", "Music", "Mystery" , "Romance" ,
            "Science-Fiction" , "TV-Movie", "Thriller", "War", "Western"};

    PrintWriter writer;

    public ImagePanel() {
        super();
        this.setPreferredSize(new Dimension(500,700));
        files = new File("./Data2").listFiles();

        JButton b1 = new JButton("Next Please");
        b1.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                nextPlease();
            }
        });

        JButton b2 = new JButton("Close Please");
        b2.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                closePlease();
            }
        });

        try{
            writer = new PrintWriter("output.txt", "UTF-8");
        }catch (Exception e) {

        }
        boxes = new JCheckBox[list.length];
        for(int i = 0 ; i < list.length ; i++) {
            boxes[i] = new JCheckBox(list[i]);
            boxes[i].setSelected(false);
            add(boxes[i]);
        }

        while(files[index].getName().charAt(0) == new Character('.'))
            index++;


        add(b1);
        add(b2);

        repaint();
    }

    @Override
    protected void paintComponent(Graphics g) {
        try {
            currentImage = files[index].getName();
            image = ImageIO.read(new File( files[index].getPath() + "/w342.jpg"));
        } catch (IOException ex) {
            writer.close();
            ex.printStackTrace();
        }

        super.paintComponent(g);
        g.drawImage(image, 50, 150, this); // see javadoc for more info on the parameters
    }

    public void nextPlease() {

        StringBuilder sb = new StringBuilder();

        for(int i = 0 ; i < list.length ; i++) {
            if(boxes[i].isSelected()) {
                sb.append(list[i]);
                sb.append(',');
            }

            boxes[i].setSelected(false);
        }

        String str = sb.toString();
        str = str.substring(0, str.length() - 1);

        writer.println(currentImage + ",{" + str + "}");
        System.out.println(currentImage + ",{" + str + "}");
        index++;

        repaint();
    }

    public void closePlease() {
        writer.close();
    }
}