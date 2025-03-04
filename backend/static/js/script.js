function addSection(sectionId, inputName) {
    const section = document.getElementById(sectionId);
  
    // Create a wrapper for the input group
    const div = document.createElement('div');
    div.className = 'input-group mb-2';
  
    // Create the input
    const input = document.createElement('input');
    input.type = 'text';
    input.name = inputName;
    input.className = 'form-control bg-dark-subtle text-light border-secondary';
    input.placeholder = 'Enter details';
  
    // Create remove button
    const removeBtn = document.createElement('button');
    removeBtn.className = 'btn btn-outline-danger border-secondary';
    removeBtn.type = 'button';
    removeBtn.textContent = 'Remove';
    removeBtn.onclick = function () {
      removeSection(removeBtn);
    };
  
    // Append to wrapper div
    div.appendChild(input);
    div.appendChild(removeBtn);
  
    // Append to section
    section.appendChild(div);
  }
  
  function removeSection(button) {
    // Remove the parent .input-group
    button.parentNode.remove();
  }
  