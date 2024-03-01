const roomId = document.currentScript.dataset.roomid;
  
  $.ajax({
    url: `/rooms/${roomId}/taken`,
    method: "GET",
    success: function (data) {
      takenDates = data.dates;
    },
    error: function (error) {
      console.error("Error fetching taken dates:", error);
    },
  });

  const dateInput1 = document.getElementById("start-date");
  const dateInput2 = document.getElementById("end-date");
  let takenDates = [];

  dateInput1.addEventListener("input", () => {
    const dateValue = new Date(dateInput1.value);

    if (dateValue < new Date()) {
      dateInput1.setCustomValidity("Please enter a date in the future.");
    } else {
      if (takenDates.includes(dateValue.toISOString().split("T")[0])) {
        dateInput1.setCustomValidity("Sorry, that date is not available for the selected room.");
      } else {
        dateInput1.setCustomValidity("");
      }
    }

    if (dateInput1.checkValidity()) {
      dateInput1.classList.remove("error");
    } else {
      dateInput1.classList.add("error");
    }
  });

  dateInput2.addEventListener("input", () => {
    const dateValue = new Date(dateInput2.value);

    if (dateValue < new Date()) {
      dateInput2.setCustomValidity("Please enter a date in the future.");
    } else {
      if (takenDates.includes(dateValue.toISOString().split("T")[0])) {
        dateInput2.setCustomValidity("Sorry, that date is not available for the selected room.");
      } else {
        dateInput2.setCustomValidity("");
      }
    }

    if (dateInput2.checkValidity()) {
      dateInput2.classList.remove("error");
    } else {
      dateInput2.classList.add("error");
    }
  });