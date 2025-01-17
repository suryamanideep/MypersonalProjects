document.querySelectorAll('.cell').forEach(cell => {
    cell.addEventListener('input', event => {
      const row = event.target.dataset.row;
      const col = event.target.dataset.col;
      const value = event.target.innerText;
      
      // Example: send data to a server or update locally
      console.log(`Row: ${row}, Col: ${col}, Value: ${value}`);
      
      // Here, you could send data to a server or store it locally as needed
    });
  });
  