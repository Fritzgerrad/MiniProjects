import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class MyCalculator implements ActionListener {
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
	Font myFont2 = new Font("Ink Free",Font.BOLD,35);
	double num1 = 5, num2 = 0, result =0;
	char operator;

	public MyCalculator() {
		frame = new JFrame("Calculator");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		frame.setSize(520, 760);
		frame.setLayout(null);
		
		textfield = new JTextField();
		textfield.setBounds(50,25,400,90);
		textfield.setFont(myFont2);
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
		// TODO Auto-generated method stub
		MyCalculator calc = new MyCalculator();
	}
	@Override
	public void actionPerformed(ActionEvent e) {
		for(int i =0; i<10;i++) {
			if(e.getSource()== numberButtons[i]) {
				textfield.setText(textfield.getText().concat(String.valueOf(i)));
				//textfield.setText(String.valueOf(num1));
			}
		}
		if (e.getSource() == decButton) {
			textfield.setText(textfield.getText().concat("."));
	
		}
		if (e.getSource() == addButton) {
			num1 = Double.parseDouble(textfield.getText());
			operator = '+';
			textfield.setText("");
		}
		if (e.getSource() == subButton) {
			num1 = Double.parseDouble(textfield.getText());
			operator = '-';
			textfield.setText("");
		}
		if (e.getSource() == mulButton) {
			num1 = Double.parseDouble(textfield.getText());
			operator = 'x';
			textfield.setText("");
		}
		if (e.getSource() == divButton) {
			num1 = Double.parseDouble(textfield.getText());
			operator = '/';
			textfield.setText("");
		}
		if (e.getSource() == sqButton) {
			num1 = Double.parseDouble(textfield.getText());
			result = num1*num1;
			textfield.setText(String.valueOf(result));
			num1 = result;
		}
		if (e.getSource() == sqrtButton) {
			num1 = Double.parseDouble(textfield.getText());
			result = Math.sqrt(num1);
			textfield.setText(String.valueOf(result));
			num1 = result;
		}
		if (e.getSource() == powerButton) {
			num1 = Double.parseDouble(textfield.getText());
			operator = 'p';
			textfield.setText("");
		}
		if (e.getSource() == modButton) {
			num1 = Double.parseDouble(textfield.getText());
			operator = 'm';
			textfield.setText("");
		}
		if (e.getSource() == recipButton) {
			num1 = Double.parseDouble(textfield.getText());
			result = 1/num1;
			textfield.setText(String.valueOf(result));
			num1 = result;
			
		}
		if (e.getSource() == rootButton) {
			num1 = Double.parseDouble(textfield.getText());
			operator = 'r';
			textfield.setText("");
			
		}if (e.getSource() == resetButton) {
			num1 = 0;
			num2 = 0;
			textfield.setText("");
			
		}if (e.getSource() == exitButton) {
			System.exit(0);
			
		}
		if (e.getSource() == eqButton) {
			num2 = Double.parseDouble(textfield.getText());
			switch(operator) {
			case '+':
				result = num1 + num2;
				break;
			case '-':
				result = num1 - num2;
				break;
			case 'x':
				result = num1 * num2;
				break;
			case '/':
				result = num1 / num2;
				break;
			case 'p':
				result = power(num1,num2);
				break;
			case 'm':
				result = num1 % num2;
				break;
			case 'r':
				result = rootOf(num2,num1);
				}
			
			textfield.setText(trimmer(String.valueOf(result)));
			num1 = result;
		}
		if (e.getSource() == clrButton) {
			textfield.setText("");
		}
		if (e.getSource() == delButton) {
			String string = textfield.getText();
			string = string.substring(0,string.length()-1);
			textfield.setText(string);
		}
		if (e.getSource() == negButton) {
			double temp = Double.parseDouble(textfield.getText());
			temp = temp*-1;
			textfield.setText(trimmer(String.valueOf(temp)));
		}
	}
	private double power(double root,double index) {
		double ans = 1;
		for (int i=0;i<index;i++) {
			ans *= root;
		}
		return ans;
	}
	private double rootOf(double root, double num) {
		double ans = 0;
		for (int k = 0;k< num/2;k++) {
			if (power(k,root)==num)
				ans = k;
			}
		return ans;
	}
	private String trimmer(String ans) {
		int stopper = ans.indexOf('.');
		String ans2 = ans.substring(stopper+1,ans.length());
		for (int i = 0;i < ans2.length();i++) {
			if (ans2.charAt(i) != '0') {
				return fit(ans);
			}
		}
		return ans.substring(0,stopper);
	}
	private String fit(String ans) {
		if(ans.length() > 11) {
			int lim = Integer.parseInt(String.valueOf(ans.charAt(12)));
			if (lim >4) {
				int stop = Integer.parseInt(String.valueOf(ans.charAt(11))) +1;
				return ans.substring(0,10)+stop;
			}
			else {
				return ans.substring(0,11);
			}
		}
		else {
			return ans;
		}
		
	}
}
