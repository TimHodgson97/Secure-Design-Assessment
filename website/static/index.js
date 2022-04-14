//function to delete opperational check note
function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }

//function to delete service record note
function deleteService(serviceId) {
    fetch("/delete-service", {
      method: "POST",
      body: JSON.stringify({ serviceId: serviceId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }

//function to delete software upgrade note
function deleteUpgrade(upgradeId) {
    fetch("/delete-upgrade", {
      method: "POST",
      body: JSON.stringify({ upgradeId: upgradeId }),
    }).then((_res) => {
      window.location.href = "/";
    });
}

//function to delete vessel repair note
function deleteRepair(repairId) {
    fetch("/delete-repair", {
      method: "POST",
      body: JSON.stringify({ repairId: repairId }),
    }).then((_res) => {
      window.location.href = "/";
    });
}

//function to delete safety inspaction note
function deleteSafety(safetyId) {
    fetch("/delete-safety", {
      method: "POST",
      body: JSON.stringify({ safetyId: safetyId }),
    }).then((_res) => {
      window.location.href = "/";
    });
}