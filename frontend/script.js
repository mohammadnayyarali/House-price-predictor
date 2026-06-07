const form = document.getElementById("prediction-form");
const predictionText = document.getElementById("prediction-text");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  predictionText.textContent = "Calculating price...";

  const payload = {
    area: Number(form.area.value),
    bedrooms: Number(form.bedrooms.value),
    bathrooms: Number(form.bathrooms.value),
    year_built: Number(form.year_built.value),
    garage: Number(form.garage.value),
    lot_size: Number(form.lot_size.value),
    location: form.location.value,
  };

  try {
    const response = await fetch("/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    if (!response.ok) {
      const error = await response.json();
      throw new Error(error.detail || error.message || "Prediction failed");
    }

    const result = await response.json();
    predictionText.textContent = `$${result.price.toLocaleString()}`;
  } catch (error) {
    predictionText.textContent = `Unable to calculate price. ${error.message || "Try again."}`;
    console.error(error);
  }
});
