
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class Calculator implements ActionListener{

	JFrame frame;
	JTextField textfield;
	JButton [] numberButtons = new JButton[10];
	JButton [] functionButtons = new JButton[17];
	JButton addButton, subButton,mulButton,divButton;
	JButton decButton, eqButton, delButton, clrButton,negButton;
	JButton sqrtButton, resetButton, sqButton, modButton;
	JButton powerButton, recipButton, rootButton, exitButton;
	JPanel panel;
	
	Font myFont = new Font("Ink Free",Font.BOLD,15);
	Font myFont1 = new Font("Ink Free",Font.BOLD,25);
	double num1 = 5, num2 = 0, result =0;
	char operator;

	
	Calculator(){
		frame = new JFrame("Calculator");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setSize(520, 760);
		frame.setLayout(null);
		
		textfield = new JTextField();
		textfield.setBounds(50,25,400,90);
		textfield.setFont(myFont);
		textfield.setEditable(false);
		
		addButton = new JButton("+");
		subButton = new JButton("-");
		mulButton = new JButton("x");
		divButton = new JButton("/");
		decButton = new JButton(".");
		eqButton = new JButton("=");
		delButton = new JButton("DEL");
		clrButton = new JButton("CLR");
		negButton = new JButton("+/-");
		resetButton = new JButton ("AC");
		sqrtButton = new JButton ("x rt 2");
		sqButton = new JButton ("x^2");
		modButton = new JButton ("mod");
		powerButton = new JButton ("x^y");
		rootButton = new JButton ("x rt y");
		recipButton = new JButton ("1/x");
		exitButton = new JButton ("EXIT");
		
		functionButtons[0] = addButton;
		functionButtons[1] = subButton;
		functionButtons[2] = mulButton;
		functionButtons[3] = divButton;
		functionButtons[4] = decButton;
		functionButtons[5] = eqButton;
		functionButtons[6] = delButton;
		functionButtons[7] = clrButton;
		functionButtons[8] = negButton;
		functionButtons[9] = resetButton;
		functionButtons[10] = exitButton;
		
		functionButtons[11] = sqButton;
		functionButtons[12] = modButton;
		functionButtons[13] = powerButton;
		functionButtons[14] = rootButton;
		functionButtons[15] = recipButton;
		functionButtons[16] = sqrtButton;
		
		
		for(int i=0;i<11;i++) {
			functionButtons[i].addActionListener(this);
			functionButtons[i].setFont(myFont1);
			functionButtons[i].setFocusable(false);
		}
		
		for(int i=11;i<17;i++) {
			functionButtons[i].addActionListener(this);
			functionButtons[i].setFont(myFont);
			functionButtons[i].setFocusable(false);
		}
		
		for(int i=0;i<10;i++) {
			numberButtons[i] = new JButton(String.valueOf(i));
			numberButtons[i].addActionListener(this);
			numberButtons[i].setFont(myFont1);
			numberButtons[i].setFocusable(false);
		}
		
		//negButton.setBounds(50,430,100,50);
		resetButton.setBounds(50,140,128,70);
		clrButton.setBounds(185, 140, 128, 70);
		exitButton.setBounds(320, 140, 128, 70);
		
		panel = new JPanel();
		panel.setBounds(50, 225, 400, 400);
		panel.setLayout(new GridLayout(6,4,15,15));
		//panel.setBackground(Color.GRAY);

		panel.add(powerButton);
		panel.add(recipButton);
		panel.add(rootButton);
		panel.add(delButton);
		panel.add(sqButton);
		panel.add(modButton);
		panel.add(sqrtButton);
		panel.add(divButton);
		panel.add(numberButtons[7]);
		panel.add(numberButtons[8]);
		panel.add(numberButtons[9]);
		panel.add(mulButton);
		panel.add(numberButtons[4]);
		panel.add(numberButtons[5]);
		panel.add(numberButtons[6]);
		panel.add(subButton);
		panel.add(numberButtons[1]);
		panel.add(numberButtons[2]);
		panel.add(numberButtons[3]);
		panel.add(addButton);
		panel.add(negButton);
		panel.add(numberButtons[0]);
		panel.add(decButton);
		panel.add(eqButton);
		
		
		
		frame.add(panel);
		frame.add(resetButton);
		frame.add(clrButton);
		frame.add(exitButton);
		frame.add(textfield);
		frame.setVisible(true);
		
	}
	
	public static void main(String[] args) {
		
		Calculator calc = new Calculator();
	}
	
	@Override
	public void actionPerformed(ActionEvent e) {
		
		for(int i =0; i<10;i++) {
			if(e.getSource()== numberButtons[i]) {
				textfield.setText(textfield.getText().concat(String.valueOf(i)));
				//textfield.setText(String.valueOf(num1));
			}
		}
		if(e.getSource()==decButton) {
			textfield.setText(textfield.getText().concat("."));
		}
		if(e.getSource()==addButton) {
			num1 = Double.parseDouble(textfield.getText());
			operator ='+';
			textfield.setText("");
		}
		if(e.getSource()==subButton) {
			num1 = Double.parseDouble(textfield.getText());
			operator ='-';
			textfield.setText("");
		}
		if(e.getSource()==mulButton) {
			num1 = Double.parseDouble(textfield.getText());
			operator ='*';
			textfield.setText("");
		}
		if(e.getSource()==divButton) {
			num1 = Double.parseDouble(textfield.getText());
			operator ='/';
			textfield.setText("");
		}
		if(e.getSource()==eqButton) {
			num2=Double.parseDouble(textfield.getText());
			
			switch(operator) {
			case'+':
				result=num1+num2;
				break;
			case'-':
				result=num1-num2;
				break;
			case'*':
				result=num1*num2;
				break;
			case'/':
				result=num1/num2;
				break;
			}
			textfield.setText(String.valueOf(result));
			num1=result;
		}
		if(e.getSource()==clrButton) {
			textfield.setText("");
		}
		if(e.getSource()==delButton) {
			String string = textfield.getText();
			textfield.setText("");
			for(int i=0;i<string.length()-1;i++) {
				textfield.setText(textfield.getText()+string.charAt(i));
			}
		}
		if(e.getSource()==negButton) {
			double temp = Double.parseDouble(textfield.getText());
			temp*=-1;
			textfield.setText(String.valueOf(temp));
		}
	}
}
