namespace AlgoritmosBusca
{
    partial class MainWindow
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainWindow));
            this.pictureBox1 = new System.Windows.Forms.PictureBox();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.limparLinhas = new System.Windows.Forms.Button();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.resultadoTextBox = new System.Windows.Forms.TextBox();
            this.calcularButton = new System.Windows.Forms.Button();
            this.limiteTextBox = new System.Windows.Forms.TextBox();
            this.aStarButton = new System.Windows.Forms.RadioButton();
            this.origemComboBox = new System.Windows.Forms.ComboBox();
            this.greedyButton = new System.Windows.Forms.RadioButton();
            this.label3 = new System.Windows.Forms.Label();
            this.custoUniformeButton = new System.Windows.Forms.RadioButton();
            this.destinoComboBox = new System.Windows.Forms.ComboBox();
            this.bidirecionalButton = new System.Windows.Forms.RadioButton();
            this.label2 = new System.Windows.Forms.Label();
            this.aprofundamentoIterativoButton = new System.Windows.Forms.RadioButton();
            this.label1 = new System.Windows.Forms.Label();
            this.profundidadeLimitadaButton = new System.Windows.Forms.RadioButton();
            this.profundidadeButton = new System.Windows.Forms.RadioButton();
            this.amplitudeButton = new System.Windows.Forms.RadioButton();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).BeginInit();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // pictureBox1
            // 
            this.pictureBox1.Image = ((System.Drawing.Image)(resources.GetObject("pictureBox1.Image")));
            this.pictureBox1.Location = new System.Drawing.Point(12, 12);
            this.pictureBox1.Name = "pictureBox1";
            this.pictureBox1.Size = new System.Drawing.Size(816, 725);
            this.pictureBox1.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pictureBox1.TabIndex = 0;
            this.pictureBox1.TabStop = false;
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.limparLinhas);
            this.groupBox1.Controls.Add(this.groupBox2);
            this.groupBox1.Controls.Add(this.calcularButton);
            this.groupBox1.Controls.Add(this.limiteTextBox);
            this.groupBox1.Controls.Add(this.aStarButton);
            this.groupBox1.Controls.Add(this.origemComboBox);
            this.groupBox1.Controls.Add(this.greedyButton);
            this.groupBox1.Controls.Add(this.label3);
            this.groupBox1.Controls.Add(this.custoUniformeButton);
            this.groupBox1.Controls.Add(this.destinoComboBox);
            this.groupBox1.Controls.Add(this.bidirecionalButton);
            this.groupBox1.Controls.Add(this.label2);
            this.groupBox1.Controls.Add(this.aprofundamentoIterativoButton);
            this.groupBox1.Controls.Add(this.label1);
            this.groupBox1.Controls.Add(this.profundidadeLimitadaButton);
            this.groupBox1.Controls.Add(this.profundidadeButton);
            this.groupBox1.Controls.Add(this.amplitudeButton);
            this.groupBox1.Location = new System.Drawing.Point(834, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(367, 725);
            this.groupBox1.TabIndex = 1;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Método de buscas";
            // 
            // limparLinhas
            // 
            this.limparLinhas.Location = new System.Drawing.Point(296, 419);
            this.limparLinhas.Name = "limparLinhas";
            this.limparLinhas.Size = new System.Drawing.Size(65, 23);
            this.limparLinhas.TabIndex = 17;
            this.limparLinhas.Text = "Limpar";
            this.limparLinhas.UseVisualStyleBackColor = true;
            this.limparLinhas.Click += new System.EventHandler(this.OnLimparLinhasClick);
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.resultadoTextBox);
            this.groupBox2.Location = new System.Drawing.Point(6, 448);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(361, 271);
            this.groupBox2.TabIndex = 16;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "Resultado";
            // 
            // resultadoTextBox
            // 
            this.resultadoTextBox.Location = new System.Drawing.Point(9, 22);
            this.resultadoTextBox.Multiline = true;
            this.resultadoTextBox.Name = "resultadoTextBox";
            this.resultadoTextBox.ReadOnly = true;
            this.resultadoTextBox.Size = new System.Drawing.Size(346, 243);
            this.resultadoTextBox.TabIndex = 15;
            // 
            // calcularButton
            // 
            this.calcularButton.Location = new System.Drawing.Point(6, 419);
            this.calcularButton.Name = "calcularButton";
            this.calcularButton.Size = new System.Drawing.Size(75, 23);
            this.calcularButton.TabIndex = 14;
            this.calcularButton.Text = "Calcular";
            this.calcularButton.UseVisualStyleBackColor = true;
            this.calcularButton.Click += new System.EventHandler(this.OnCalcularButtonClick);
            // 
            // limiteTextBox
            // 
            this.limiteTextBox.Enabled = false;
            this.limiteTextBox.Location = new System.Drawing.Point(59, 340);
            this.limiteTextBox.Name = "limiteTextBox";
            this.limiteTextBox.Size = new System.Drawing.Size(121, 23);
            this.limiteTextBox.TabIndex = 13;
            // 
            // aStarButton
            // 
            this.aStarButton.AutoSize = true;
            this.aStarButton.Location = new System.Drawing.Point(6, 197);
            this.aStarButton.Name = "aStarButton";
            this.aStarButton.Size = new System.Drawing.Size(70, 19);
            this.aStarButton.TabIndex = 7;
            this.aStarButton.Text = "A Estrela";
            this.aStarButton.UseVisualStyleBackColor = true;
            // 
            // origemComboBox
            // 
            this.origemComboBox.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.origemComboBox.FormattingEnabled = true;
            this.origemComboBox.Location = new System.Drawing.Point(59, 282);
            this.origemComboBox.Name = "origemComboBox";
            this.origemComboBox.Size = new System.Drawing.Size(202, 23);
            this.origemComboBox.TabIndex = 8;
            // 
            // greedyButton
            // 
            this.greedyButton.AutoSize = true;
            this.greedyButton.Location = new System.Drawing.Point(6, 172);
            this.greedyButton.Name = "greedyButton";
            this.greedyButton.Size = new System.Drawing.Size(62, 19);
            this.greedyButton.TabIndex = 6;
            this.greedyButton.Text = "Greedy";
            this.greedyButton.UseVisualStyleBackColor = true;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(6, 343);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(40, 15);
            this.label3.TabIndex = 12;
            this.label3.Text = "Limite";
            // 
            // custoUniformeButton
            // 
            this.custoUniformeButton.AutoSize = true;
            this.custoUniformeButton.Location = new System.Drawing.Point(6, 147);
            this.custoUniformeButton.Name = "custoUniformeButton";
            this.custoUniformeButton.Size = new System.Drawing.Size(109, 19);
            this.custoUniformeButton.TabIndex = 5;
            this.custoUniformeButton.Text = "Custo Uniforme";
            this.custoUniformeButton.UseVisualStyleBackColor = true;
            // 
            // destinoComboBox
            // 
            this.destinoComboBox.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.destinoComboBox.FormattingEnabled = true;
            this.destinoComboBox.Location = new System.Drawing.Point(59, 311);
            this.destinoComboBox.Name = "destinoComboBox";
            this.destinoComboBox.Size = new System.Drawing.Size(202, 23);
            this.destinoComboBox.TabIndex = 9;
            // 
            // bidirecionalButton
            // 
            this.bidirecionalButton.AutoSize = true;
            this.bidirecionalButton.Location = new System.Drawing.Point(6, 122);
            this.bidirecionalButton.Name = "bidirecionalButton";
            this.bidirecionalButton.Size = new System.Drawing.Size(87, 19);
            this.bidirecionalButton.TabIndex = 4;
            this.bidirecionalButton.Text = "Bidirecional";
            this.bidirecionalButton.UseVisualStyleBackColor = true;
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(6, 314);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(47, 15);
            this.label2.TabIndex = 11;
            this.label2.Text = "Destino";
            // 
            // aprofundamentoIterativoButton
            // 
            this.aprofundamentoIterativoButton.AutoSize = true;
            this.aprofundamentoIterativoButton.Location = new System.Drawing.Point(6, 97);
            this.aprofundamentoIterativoButton.Name = "aprofundamentoIterativoButton";
            this.aprofundamentoIterativoButton.Size = new System.Drawing.Size(170, 19);
            this.aprofundamentoIterativoButton.TabIndex = 3;
            this.aprofundamentoIterativoButton.Text = "Aprofundamento Interativo";
            this.aprofundamentoIterativoButton.UseVisualStyleBackColor = true;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(6, 285);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(47, 15);
            this.label1.TabIndex = 10;
            this.label1.Text = "Origem";
            // 
            // profundidadeLimitadaButton
            // 
            this.profundidadeLimitadaButton.AutoSize = true;
            this.profundidadeLimitadaButton.Location = new System.Drawing.Point(6, 72);
            this.profundidadeLimitadaButton.Name = "profundidadeLimitadaButton";
            this.profundidadeLimitadaButton.Size = new System.Drawing.Size(146, 19);
            this.profundidadeLimitadaButton.TabIndex = 2;
            this.profundidadeLimitadaButton.Text = "Profundidade Limitada";
            this.profundidadeLimitadaButton.UseVisualStyleBackColor = true;
            this.profundidadeLimitadaButton.CheckedChanged += new System.EventHandler(this.OnProfundidadeLimitadaCheck);
            // 
            // profundidadeButton
            // 
            this.profundidadeButton.AutoSize = true;
            this.profundidadeButton.Location = new System.Drawing.Point(6, 47);
            this.profundidadeButton.Name = "profundidadeButton";
            this.profundidadeButton.Size = new System.Drawing.Size(97, 19);
            this.profundidadeButton.TabIndex = 1;
            this.profundidadeButton.Text = "Profundidade";
            this.profundidadeButton.UseVisualStyleBackColor = true;
            // 
            // amplitudeButton
            // 
            this.amplitudeButton.AutoSize = true;
            this.amplitudeButton.Checked = true;
            this.amplitudeButton.Location = new System.Drawing.Point(6, 22);
            this.amplitudeButton.Name = "amplitudeButton";
            this.amplitudeButton.Size = new System.Drawing.Size(81, 19);
            this.amplitudeButton.TabIndex = 0;
            this.amplitudeButton.TabStop = true;
            this.amplitudeButton.Text = "Amplitude";
            this.amplitudeButton.UseVisualStyleBackColor = true;
            // 
            // MainWindow
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 15F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1208, 742);
            this.Controls.Add(this.groupBox1);
            this.Controls.Add(this.pictureBox1);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.MaximizeBox = false;
            this.Name = "MainWindow";
            this.ShowIcon = false;
            this.Text = "Algoritmos de Busca";
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox1)).EndInit();
            this.groupBox1.ResumeLayout(false);
            this.groupBox1.PerformLayout();
            this.groupBox2.ResumeLayout(false);
            this.groupBox2.PerformLayout();
            this.ResumeLayout(false);

        }

        #endregion

        private PictureBox pictureBox1;
        private GroupBox groupBox1;
        private Label label1;
        private ComboBox destinoComboBox;
        private ComboBox origemComboBox;
        private RadioButton aStarButton;
        private RadioButton greedyButton;
        private RadioButton custoUniformeButton;
        private RadioButton bidirecionalButton;
        private RadioButton aprofundamentoIterativoButton;
        private RadioButton profundidadeLimitadaButton;
        private RadioButton profundidadeButton;
        private RadioButton amplitudeButton;
        private TextBox limiteTextBox;
        private Label label3;
        private Label label2;
        private GroupBox groupBox2;
        private TextBox resultadoTextBox;
        private Button calcularButton;
        private Button limparLinhas;
    }
}