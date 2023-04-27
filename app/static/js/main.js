document.addEventListener("DOMContentLoaded", function () {
    const submitButton = document.getElementById("submit-button");
    const companyNameInput = document.getElementById("company-name-input");
    const kpiContainer = document.getElementById("kpi-container");
    const chartContainer = document.getElementById("chart-container");
  
    function createKpiElement(kpiData) {
      const kpiElement = document.createElement("div");
      kpiElement.classList.add("kpi");
  
      const title = document.createElement("h3");
      title.textContent = kpiData.name;
      kpiElement.appendChild(title);
  
      const value = document.createElement("p");
      value.textContent = parseFloat(kpiData.value).toFixed(2);
      kpiElement.appendChild(value);
  
      return kpiElement; // Make sure to return kpiElement
    }
  
    function drawChart(data, companyName) {
      // ...
    }
  
    submitButton.addEventListener("click", async function () {
      const companyName = companyNameInput.value;
      if (!companyName) {
        alert("Please enter a company name.");
        return;
      }
  
      try {
        const response = await fetch("/api/data", {
          method: "POST",
          body: JSON.stringify({ company_name: companyName }),
          headers: { "Content-Type": "application/json" },
        });
  
        const data = await response.json();
        const kpiData = data.kpiData;
        const chartData = data.chartData;
  
        kpiContainer.innerHTML = "";
        chartContainer.innerHTML = "";
  
        kpiData.forEach((kpi) => {
          const kpiElement = createKpiElement(kpi);
          kpiContainer.appendChild(kpiElement);
        });
  
        const canvas = document.createElement("canvas");
        canvas.id = "myChart";
        chartContainer.appendChild(canvas);
  
        drawChart(chartData, companyName);
      } catch (error) {
        console.error(error);
        alert("Failed to fetch data. Please check the console for more information.");
      }
    });
  });
  