function updateProgress(step) {
    let progressBar = document.querySelector('.progress-bar');
    let progressValue = 0;
    if (step === 1) {
      progressValue = 33;
    } else if (step === 2) {
      progressValue = 66;
    } else if (step === 3) {
      progressValue = 100;
    }
    progressBar.style.width = progressValue + '%';
    progressBar.setAttribute('aria-valuenow', progressValue);
  }
  