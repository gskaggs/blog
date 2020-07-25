function toggleHiddenElement(hiddenElemID, buttonElemID) {
    var hiddenElem = document.getElementById(hiddenElemID);
    var buttonElem = document.getElementById(buttonElemID);
    if (hiddenElem.style.display === "none") {
      hiddenElem.style.display = "block";
      buttonElem.innerHTML = "Hide Notes";
    } else {
      hiddenElem.style.display = "none";
      buttonElem.innerHTML = "Show Notes";
    }
  }