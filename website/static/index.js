function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }

function deleteService(serviceId) {
    fetch("/delete-service", {
      method: "POST",
      body: JSON.stringify({ serviceId: serviceId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }

function deleteUpgrade(upgradeId) {
    fetch("/delete-upgrade", {
      method: "POST",
      body: JSON.stringify({ upgradeId: upgradeId }),
    }).then((_res) => {
      window.location.href = "/";
    });
}

function deleteRepair(repairId) {
    fetch("/delete-repair", {
      method: "POST",
      body: JSON.stringify({ repairId: repairId }),
    }).then((_res) => {
      window.location.href = "/";
    });
}

function deleteSafety(safetyId) {
    fetch("/delete-safety", {
      method: "POST",
      body: JSON.stringify({ safetyId: safetyId }),
    }).then((_res) => {
      window.location.href = "/";
    });
}