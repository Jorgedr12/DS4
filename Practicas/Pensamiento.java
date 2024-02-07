import java.awt.BorderLayout;
import java.awt.Dimension;

import javax.swing.JButton;
import javax.swing.JDialog;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JProgressBar;
import javax.swing.JTextField;

public class Pensamiento {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Mi Frame");
        frame.setSize(300, 250);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
        frame.setLayout(null);
        frame.setResizable(false);
        frame.setLocationRelativeTo(null);
        

        JLabel label = new JLabel("Piensa en un numero del 1 al 10");
        label.setBounds(50, 15, 300, 30);
        frame.add(label);

        JTextField text = new JTextField();
        text.setBounds(40, 70, 200, 30);
        frame.add(text);

        JButton button = new JButton("Read my mind");
        button.setBounds(40, 120, 200, 30);
        frame.add(button);
        button.addActionListener(e -> {

                JProgressBar progressBar = new JProgressBar(0, 100);
                progressBar.setStringPainted(true);
                JLabel messageLabel = new JLabel();
                JPanel panel = new JPanel(new BorderLayout());
                panel.setPreferredSize(new Dimension(300, 30));
                panel.add(progressBar, BorderLayout.SOUTH);
                panel.add(messageLabel, BorderLayout.NORTH); 
                messageLabel.setText("Analizando el pensamiento..."); 
                JOptionPane progressDialog = new JOptionPane(panel, JOptionPane.INFORMATION_MESSAGE, JOptionPane.DEFAULT_OPTION, null, new Object[]{}, null);
                JDialog dialog = progressDialog.createDialog(frame, "Progreso");
            
            Thread progressThread = new Thread(() -> {
                for (int i = 0; i <= 100; i++) {
                    progressBar.setValue(i);
                    if (i==25) {
                        messageLabel.setText("Procesando la memoria..."); 
                    }
                    if (i==50) {
                        messageLabel.setText("Renderizando conexión cognitiva...");
                    }
                    if (i==75) {
                        messageLabel.setText("Proyeccion cerebral casi completa..."); 
                    }
                    try {
                        Thread.sleep(100);
                    } catch (InterruptedException ex) {
                        ex.printStackTrace();
                    }
                }
                
                dialog.dispose();
                JOptionPane.showMessageDialog(frame, "Pensaste en el numero: " + text.getText());
            });
            progressThread.start();
            
            dialog.setVisible(true);
        });
        
    }

}
