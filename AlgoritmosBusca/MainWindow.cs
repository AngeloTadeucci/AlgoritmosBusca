using IronPython.Hosting;

namespace AlgoritmosBusca;

public partial class MainWindow : Form
{
    private readonly Dictionary<string, Point> nodes = new()
    {
        { "ABANDONED STATE BUILDING", new Point(651, 307) },
        { "ARCANA PLATEAU", new Point(620, 366) },
        { "AURORA LAKE", new Point(86, 459) },
        { "BIOME RESEARCH LAB", new Point(368, 182) },
        { "BIOME TEST SITE", new Point(400, 131) },
        { "BONNEVILLE", new Point(180, 432) },
        { "DUMPING GROUND", new Point(427, 305) },
        { "FIELDS OF PERKAU", new Point(464, 223) },
        { "FORAIN FOREST", new Point(216, 665) },
        { "JUPIA ROAD", new Point(620, 46) },
        { "KIDEL AETHERINE PLANT", new Point(211, 250) },
        { "KIDEL CROSSING", new Point(307, 508) },
        { "KIDEL TAIREN BASE", new Point(246, 295) },
        { "LESHY FOREST", new Point(523, 149) },
        { "MANNSTAND FORTRESS", new Point(681, 240) },
        { "RANMELLE", new Point(241, 563) },
        { "RICHMONDE", new Point(277, 644) },
        { "SAFEHOLD DEFENSE LINE", new Point(306, 320) },
        { "SAFEHOLD", new Point(337, 417) },
        { "TAIREN ROBOT FACTORY", new Point(560, 73) },
        { "TIAMAN", new Point(650, 170) },
        { "WRAITH'S FOOTHOLD", new Point(464, 56) },
        { "ZEKEBEN ROAD", new Point(497, 384) },
    };

    private List<string> LastResult = new List<string>();

    public MainWindow()
    {
        InitializeComponent();
        PopulateComboBox();
    }

    private void OnCalcularButtonClick(object sender, EventArgs e)
    {
        int limite = 0;
        if (profundidadeLimitadaButton.Checked)
        {
            string text = limiteTextBox.Text.Trim();
            if (string.IsNullOrEmpty(text))
            {
                NotifyMessage("Use algum valor para o limite.");
                return;
            }

            if (!int.TryParse(text, out limite))
            {
                NotifyMessage("Digite somente números para o limite.");
                return;
            }
        }

        if (origemComboBox.SelectedIndex == -1)
        {
            NotifyMessage("Selecione algum node de origem!");
            return;
        }

        if (destinoComboBox.SelectedIndex == -1)
        {
            NotifyMessage("Selecione algum node de destino!");
            return;
        }

        if (destinoComboBox.SelectedIndex == origemComboBox.SelectedIndex)
        {
            NotifyMessage("A origem é igual ao destino!");
            return;
        }

        var engine = Python.CreateEngine();
        var scope = engine.CreateScope();
        string script;

        if (amplitudeButton.Checked || profundidadeButton.Checked || profundidadeLimitadaButton.Checked || aprofundamentoIterativoButton.Checked || bidirecionalButton.Checked)
        {
            script = "D:/Projetos/Unitau/AlgoritmosBusca/AlgoritmosBusca/busca_sem_info_6ADS.py";
        }
        else
        {
            script = "D:/Projetos/Unitau/AlgoritmosBusca/AlgoritmosBusca/busca_com_pesos_6ADS.py";
        }

        engine.ExecuteFile(script, scope);

        dynamic? function = null;
        if (amplitudeButton.Checked)
        {
            function = scope.GetVariable("runAmplitude");
        }
        else if (profundidadeButton.Checked)
        {
            function = scope.GetVariable("runProfundidade");
        }
        else if (profundidadeLimitadaButton.Checked)
        {
            function = scope.GetVariable("runProfundidadeLimitada");
        }
        else if (aprofundamentoIterativoButton.Checked)
        {
            function = scope.GetVariable("runAprofundamentoIterativo");
        }
        else if (bidirecionalButton.Checked)
        {
            function = scope.GetVariable("runBidirecional");
        }
        else if (custoUniformeButton.Checked)
        {
            function = scope.GetVariable("runCustoUniforme");
        }
        else if (greedyButton.Checked)
        {
            function = scope.GetVariable("runGreedy");
        }
        else if (aStarButton.Checked)
        {
            function = scope.GetVariable("runAEstrela");
        }

        if (function is null)
        {
            return;
        }

        dynamic result;
        if (profundidadeLimitadaButton.Checked)
        {
            result = function(origemComboBox.Text, destinoComboBox.Text, limite);
        }
        else
        {
            result = function(origemComboBox.Text, destinoComboBox.Text);
        }

        List<string> caminho = new List<string>();
        if (amplitudeButton.Checked || profundidadeButton.Checked || profundidadeLimitadaButton.Checked || aprofundamentoIterativoButton.Checked || bidirecionalButton.Checked)
        {
            if (result is IronPython.Runtime.List)
            {
                foreach (var item in result)
                {
                    caminho.Add(item);
                }
                resultadoTextBox.Text = $"Caminho: {string.Join(", ", caminho)}";
            }
            else
            {
                resultadoTextBox.Text = $"Caminho: caminho não encontrado";
            }
        }
        else
        {
            caminho = ReverseIronPythonList(result[0]);
            resultadoTextBox.Text = $"Caminho: {string.Join(", ", caminho)} \r\nCusto: {result[1]}";
        }

        pictureBox1.Refresh();
        DrawLines(caminho);
    }

    private void DrawLines(List<string> caminho)
    {
        Graphics graphic = pictureBox1.CreateGraphics();
        Pen pen = new Pen(Color.Red, 5);

        for (int i = 0; i < caminho.Count - 1; i++)
        {
            Point first = nodes[caminho[i]];
            Point second = nodes[caminho[i + 1]];
            graphic.DrawLine(pen, first, second);
        }
        LastResult = caminho;
    }

    private List<string> ReverseIronPythonList(dynamic list)
    {
        List<string> newList = new List<string>();
        for (int i = list.Count - 1; i >= 0; i--)
        {
            newList.Add(list[i]);
        }
        return newList;
    }

    private void PopulateComboBox()
    {
        destinoComboBox.Items.AddRange(nodes.Keys.ToArray());
        origemComboBox.Items.AddRange(nodes.Keys.ToArray());
    }

    private void OnProfundidadeLimitadaCheck(object sender, EventArgs e)
    {
        if (sender is not RadioButton rb)
        {
            return;
        }

        limiteTextBox.Enabled = rb.Checked;
    }

    private void NotifyMessage(string sText, MessageBoxIcon eIcon = MessageBoxIcon.None)
    {
        MessageBox.Show(this, sText, Text, MessageBoxButtons.OK, eIcon);
    }

    private void OnLimparLinhasClick(object sender, EventArgs e)
    {
        pictureBox1.Refresh();
        resultadoTextBox.Text = string.Empty;
    }
}
