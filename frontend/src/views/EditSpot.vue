<template>
  <div class="edit-spot">
    <!-- Background Pattern -->
    <div class="bg-pattern"></div>
    
    <!-- Main Container -->
    <div class="edit-container">
      <!-- Header Section -->
      <div class="header-section">
        <div class="parking-icon">
          <svg viewBox="0 0 100 100" class="icon">
            <rect x="10" y="20" width="80" height="60" rx="5" fill="none" stroke="currentColor" stroke-width="3"/>
            <rect x="20" y="30" width="15" height="25" rx="2" fill="currentColor"/>
            <rect x="42.5" y="30" width="15" height="25" rx="2" fill="currentColor"/>
            <rect x="65" y="30" width="15" height="25" rx="2" fill="currentColor"/>
            <text x="50" y="70" text-anchor="middle" font-size="12" fill="currentColor" font-weight="bold">P</text>
            <!-- Edit Icon -->
            <path d="M75 15 L85 25 L75 35" stroke="currentColor" stroke-width="2" fill="none"/>
            <circle cx="85" cy="25" r="3" fill="currentColor"/>
          </svg>
        </div>
        <h2 class="page-title">
          <span class="gradient-text">Edit Parking Spot</span>
        </h2>
        <p class="page-subtitle">Manage spot details and status</p>
      </div>

      <!-- Loading State -->
      <div v-if="!spot" class="loading-section">
        <div class="loading-spinner">
          <div class="spinner"></div>
        </div>
        <p class="loading-text">Loading spot details...</p>
      </div>

      <!-- Spot Details Section -->
      <div v-else class="details-section">
        <div class="info-card">
          <div class="card-header">
            <svg class="card-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <rect x="3" y="3" width="18" height="18" rx="2" ry="2"/>
              <path d="M9 9h6v6H9z"/>
            </svg>
            <h3>Spot Information</h3>
          </div>
          
          <div class="details-grid">
            <div class="detail-item spot-id-item">
              <div class="item-icon">🏷️</div>
              <div class="item-content">
                <span class="item-label">Spot ID</span>
                <span class="item-value">{{ spot.id }}</span>
              </div>
            </div>

            <div class="detail-item status-item" :class="spot.status === 'A' ? 'available-status' : 'occupied-status'">
              <div class="item-icon">
                {{ spot.status === 'A' ? '✅' : '🚗' }}
              </div>
              <div class="item-content">
                <span class="item-label">Status</span>
                <span class="item-value status-badge" :class="spot.status === 'A' ? 'badge-available' : 'badge-occupied'">
                  {{ spot.status === 'A' ? 'Available' : 'Occupied' }}
                </span>
              </div>
            </div>

            <!-- Occupied Spot Details -->
            <template v-if="spot.status !== 'A'">
              <div class="detail-item user-item">
                <div class="item-icon">👤</div>
                <div class="item-content">
                  <span class="item-label">User</span>
                  <span class="item-value">{{ spot.username || 'N/A' }}</span>
                </div>
              </div>

              <div class="detail-item vehicle-item">
                <div class="item-icon">🚙</div>
                <div class="item-content">
                  <span class="item-label">Vehicle Number</span>
                  <span class="item-value">{{ spot.vehicle_number || 'N/A' }}</span>
                </div>
              </div>

              <div class="detail-item time-item">
                <div class="item-icon">⏰</div>
                <div class="item-content">
                  <span class="item-label">Parking Time</span>
                  <span class="item-value">{{ formatDateTime(spot.parking_timestamp) }}</span>
                </div>
              </div>

              <div class="detail-item leaving-item">
                <div class="item-icon">🏁</div>
                <div class="item-content">
                  <span class="item-label">Leaving Time</span>
                  <span class="item-value">{{ spot.leaving_timestamp ? formatDateTime(spot.leaving_timestamp) : 'Not Set' }}</span>
                </div>
              </div>

              <div class="detail-item cost-item">
                <div class="item-icon">💰</div>
                <div class="item-content">
                  <span class="item-label">Estimated Cost</span>
                  <span class="item-value cost-highlight">₹{{ spot.estimated_cost || '0' }}</span>
                </div>
              </div>
            </template>
          </div>

          <div class="action-section">
            <div class="button-group">
              <!-- Delete Button (for available spots) -->
              <button 
                v-if="spot.status === 'A'" 
                class="btn btn-delete" 
                @click="deleteSpot"
              >
                <span class="btn-content">
                  <svg class="btn-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <polyline points="3,6 5,6 21,6"/>
                    <path d="m19,6v14a2,2 0 0,1 -2,2H7a2,2 0 0,1 -2,-2V6m3,0V4a2,2 0 0,1 2,-2h4a2,2 0 0,1 2,2v2"/>
                    <line x1="10" y1="11" x2="10" y2="17"/>
                    <line x1="14" y1="11" x2="14" y2="17"/>
                  </svg>
                  Delete Spot
                </span>
                <div class="btn-shimmer"></div>
              </button>
              
              <!-- Show Details Button (for occupied spots) -->
              <button 
                v-if="spot.status !== 'A'" 
                class="btn btn-details" 
                @click="showOccupiedDetails"
              >
                <span class="btn-content">
                  <svg class="btn-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="10"/>
                    <line x1="12" y1="16" x2="12" y2="12"/>
                    <line x1="12" y1="8" x2="12.01" y2="8"/>
                  </svg>
                  Show Full Details
                </span>
                <div class="btn-shimmer"></div>
              </button>
              
              <!-- Close Button -->
              <button class="btn btn-close" @click="goBack">
                <span class="btn-content">
                  <svg class="btn-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
                    <polyline points="9,22 9,12 15,12 15,22"/>
                  </svg>
                  Back to Dashboard
                </span>
                <div class="btn-shimmer"></div>
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Floating Decorative Elements -->
      <div class="floating-elements">
        <div class="float-shape shape-1"></div>
        <div class="float-shape shape-2"></div>
        <div class="float-shape shape-3"></div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "EditSpot",
  data() {
    return { 
      spot: null 
    };
  },
  async created() {
    await this.loadSpotDetails();
  },
  methods: {
    async loadSpotDetails() {
      const { lotId, spotNum } = this.$route.params;
      const token = localStorage.getItem("auth_token");
      
      try {
        const res = await fetch(`/api/parkingspot/${lotId}/${spotNum}/details`, {
          headers: { Authorization: token }
        });
        const json = await res.json();
        
        if (res.ok && json.status === 'ok') {
          this.spot = json.spot;
        } else {
          alert(json.message || 'Spot not found');
          this.$router.go(-1);
        }
      } catch (error) {
        console.error('Error loading spot details:', error);
        alert('Error loading spot details');
        this.$router.go(-1);
      }
    },
    
    async deleteSpot() {
      if (this.spot.status !== "A") {
        alert("Only available spots can be deleted."); 
        return;
      }
      
      if (!confirm("Are you sure you want to delete this spot? This action cannot be undone.")) {
        return;
      }
      
      const deleteBtn = document.querySelector('.btn-delete');
      if (deleteBtn) {
        deleteBtn.disabled = true;
        const btnContent = deleteBtn.querySelector('.btn-content');
        if (btnContent) {
          btnContent.innerHTML = `
            <svg class="btn-icon spinner-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M21 12a9 9 0 11-6.219-8.56"/>
            </svg>
            Deleting...
          `;
        }
      }
      
      const token = localStorage.getItem("auth_token");
      
      try {
        const res = await fetch(`/api/parkingspot`, {
          method: "DELETE",
          headers: { 
            "Content-Type": "application/json", 
            Authorization: token 
          },
          body: JSON.stringify({ id: this.spot.id }),
        });
        
        const data = await res.json();
        
        if (res.ok && data.status === "ok") {
          alert("Spot deleted successfully!");
          this.$router.push("/admin-dashboard");
        } else {
          alert(data.message || "Failed to delete spot");
          if (deleteBtn) deleteBtn.disabled = false;
        }
      } catch (error) {
        console.error('Delete error:', error);
        alert("Error deleting spot");
        if (deleteBtn) deleteBtn.disabled = false;
      }
    },
    
    showOccupiedDetails() {
      const details = [
        `🆔 Spot ID: ${this.spot.id}`,
        `👤 User: ${this.spot.username || 'N/A'}`,
        `🚙 Vehicle: ${this.spot.vehicle_number || 'N/A'}`,
        `⏰ Parked At: ${this.formatDateTime(this.spot.parking_timestamp)}`,
        `🏁 Leaving At: ${this.spot.leaving_timestamp ? this.formatDateTime(this.spot.leaving_timestamp) : 'Not Set'}`,
        `💰 Estimated Cost: ₹${this.spot.estimated_cost || '0'}`
      ].join('\n\n');
      
      alert(details);
    },
    
    formatDateTime(timestamp) {
      if (!timestamp) return 'N/A';
      let date;
      if (timestamp.endsWith('Z')) {
        date = new Date(timestamp);
      } else {
        date = new Date(timestamp + 'Z');
      }
      return date.toLocaleString();
    },
    
    goBack() {
      this.$router.push("/admin-dashboard");
    }
  }
};
</script>

<style scoped>
/* Color Variables - Same as Release Spot */
:root {
  --primary-blue: #2563eb;      
  --secondary-blue: #3b82f6;    
  --accent-orange: #f59e0b;     
  --accent-purple: #8b5cf6;     
  --success-green: #10b981;     
  --pink-accent: #ec4899;       
  --cyan-accent: #06b6d4;       
  --red-accent: #ef4444;        
  --dark-gray: #1f2937;         
  --medium-gray: #6b7280;       
  --light-gray: #f3f4f6;        
  --white: #ffffff;
  --shadow: rgba(0, 0, 0, 0.1);
  --shadow-dark: rgba(0, 0, 0, 0.2);
}

.edit-spot {
  min-height: 100vh;
  background: linear-gradient(135deg, 
    var(--primary-blue) 0%, 
    var(--accent-purple) 25%, 
    var(--pink-accent) 50%, 
    var(--cyan-accent) 75%, 
    var(--success-green) 100%);
  background-size: 400% 400%;
  animation: gradientShift 12s ease infinite;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
  position: relative;
  overflow: hidden;
}

@keyframes gradientShift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

/* Animated Background Pattern */
.bg-pattern {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: 
    radial-gradient(circle at 25% 25%, rgba(255, 255, 255, 0.08) 0%, transparent 50%),
    radial-gradient(circle at 75% 75%, rgba(245, 158, 11, 0.08) 0%, transparent 50%),
    radial-gradient(circle at 50% 50%, rgba(139, 92, 246, 0.08) 0%, transparent 50%),
    repeating-linear-gradient(
      45deg,
      transparent,
      transparent 100px,
      rgba(255, 255, 255, 0.02) 102px,
      rgba(255, 255, 255, 0.02) 104px
    );
  animation: drift 25s linear infinite, pulse 8s ease-in-out infinite;
}

@keyframes drift {
  0% { transform: translate(0, 0) rotate(0deg); }
  100% { transform: translate(50px, 50px) rotate(360deg); }
}

@keyframes pulse {
  0%, 100% { opacity: 0.6; }
  50% { opacity: 1; }
}

/* Main Container */
.edit-container {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border-radius: 24px;
  padding: 50px 40px;
  max-width: 800px;
  width: 100%;
  box-shadow: 
    0 30px 100px var(--shadow-dark),
    0 0 0 1px rgba(255, 255, 255, 0.2),
    inset 0 1px 0 rgba(255, 255, 255, 0.9);
  border: 1px solid rgba(255, 255, 255, 0.3);
  position: relative;
  z-index: 1;
  animation: slideUp 0.8s ease-out;
}

@keyframes slideUp {
  from {
    opacity: 0;
    transform: translateY(50px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Header Section */
.header-section {
  text-align: center;
  margin-bottom: 40px;
  position: relative;
}

.parking-icon {
  display: inline-block;
  margin-bottom: 20px;
  background: linear-gradient(135deg, var(--success-green), var(--cyan-accent), var(--accent-orange));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: float 4s ease-in-out infinite, iconGlow 6s ease infinite;
}

.parking-icon .icon {
  width: 70px;
  height: 70px;
  filter: drop-shadow(0 4px 15px rgba(16, 185, 129, 0.3));
}

@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-10px); }
}

@keyframes iconGlow {
  0%, 100% { filter: drop-shadow(0 4px 15px rgba(16, 185, 129, 0.3)) hue-rotate(0deg); }
  33% { filter: drop-shadow(0 4px 15px rgba(6, 182, 212, 0.3)) hue-rotate(120deg); }
  66% { filter: drop-shadow(0 4px 15px rgba(245, 158, 11, 0.3)) hue-rotate(240deg); }
}

.page-title {
  font-size: 2.5em;
  font-weight: 800;
  margin-bottom: 10px;
  letter-spacing: -1px;
}

.gradient-text {
  color: #000;
  text-shadow: 0 2px 3px rgba(0, 0, 0, 0.2);
}

.page-subtitle {
  color: var(--medium-gray);
  font-size: 1.1em;
  font-weight: 500;
}

.header-section::after {
  content: '';
  position: absolute;
  bottom: -15px;
  left: 50%;
  transform: translateX(-50%);
  width: 80px;
  height: 4px;
  background: linear-gradient(90deg, 
    var(--success-green), 
    var(--cyan-accent), 
    var(--accent-orange));
  border-radius: 2px;
  animation: lineGlow 3s ease infinite;
}

@keyframes lineGlow {
  0%, 100% { opacity: 0.6; }
  50% { opacity: 1; }
}

/* Loading Section */
.loading-section {
  text-align: center;
  padding: 60px 20px;
}

.loading-spinner {
  margin-bottom: 20px;
}

.spinner {
  width: 50px;
  height: 50px;
  border: 4px solid var(--light-gray);
  border-top: 4px solid var(--primary-blue);
  border-radius: 50%;
  animation: spin 1s linear infinite;
  margin: 0 auto;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}

.loading-text {
  color: var(--medium-gray);
  font-size: 1.1em;
  font-weight: 500;
}

/* Info Card */
.info-card {
  background: linear-gradient(145deg, rgba(255, 255, 255, 0.9), rgba(243, 244, 246, 0.8));
  border-radius: 20px;
  padding: 30px;
  box-shadow: 0 15px 50px var(--shadow);
  border: 2px solid transparent;
  background-clip: padding-box;
  position: relative;
  overflow: hidden;
}

.info-card::before {
  content: '';
  position: absolute;
  inset: 0;
  padding: 2px;
  background: linear-gradient(135deg, 
    var(--success-green), 
    var(--cyan-accent), 
    var(--accent-orange), 
    var(--pink-accent));
  background-size: 400% 400%;
  border-radius: inherit;
  mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  mask-composite: exclude;
  -webkit-mask-composite: xor;
  animation: borderFlow 6s ease infinite;
}

@keyframes borderFlow {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}

.card-header {
  display: flex;
  align-items: center;
  gap: 12px;
  margin-bottom: 25px;
  padding-bottom: 15px;
  border-bottom: 2px solid var(--light-gray);
}

.card-icon {
  width: 24px;
  height: 24px;
  color: var(--primary-blue);
}

.card-header h3 {
  margin: 0;
  font-weight: 700;
  color: var(--dark-gray);
}

/* Details Grid */
.details-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
  margin-bottom: 30px;
}

.detail-item {
  display: flex;
  align-items: center;
  gap: 15px;
  background: linear-gradient(145deg, var(--white), rgba(243, 244, 246, 0.5));
  padding: 20px;
  border-radius: 16px;
  box-shadow: 0 8px 25px var(--shadow);
  border: 2px solid transparent;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.detail-item::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, 
    transparent, 
    rgba(255, 255, 255, 0.1), 
    transparent);
  transition: left 0.5s ease;
}

.detail-item:hover {
  transform: translateY(-5px) scale(1.02);
  box-shadow: 0 15px 50px var(--shadow-dark);
}

.detail-item:hover::before {
  left: 100%;
}

.detail-item:hover .item-icon {
  transform: scale(1.1) rotate(5deg);
  transition: transform 0.3s ease;
}

/* Specific item styling */
.spot-id-item { border-color: var(--primary-blue); }
.available-status { border-color: var(--success-green); }
.occupied-status { border-color: var(--red-accent); }
.user-item { border-color: var(--accent-purple); }
.vehicle-item { border-color: var(--cyan-accent); }
.time-item { border-color: var(--accent-orange); }
.leaving-item { border-color: var(--pink-accent); }
.cost-item { 
  border-color: var(--accent-orange); 
  background: linear-gradient(145deg, rgba(245, 158, 11, 0.05), rgba(236, 72, 153, 0.05));
}

.item-icon {
  font-size: 2em;
  background: linear-gradient(135deg, var(--primary-blue), var(--accent-purple));
  border-radius: 12px;
  padding: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  min-width: 50px;
  height: 50px;
  box-shadow: 0 4px 15px var(--shadow);
}

.item-content {
  flex: 1;
}

.item-label {
  display: block;
  font-size: 0.85em;
  color: var(--medium-gray);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  margin-bottom: 4px;
}

.item-value {
  display: block;
  font-size: 1.1em;
  font-weight: 700;
  color: var(--dark-gray);
}

.status-badge {
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 0.9em;
  font-weight: 700;
  text-transform: uppercase;
}

.badge-available {
  background: linear-gradient(135deg, var(--success-green), var(--cyan-accent));
  color: var(--white);
}

.badge-occupied {
  background: linear-gradient(135deg, var(--red-accent), var(--pink-accent));
  color: var(--white);
}

.cost-highlight {
  font-size: 1.3em;
  font-weight: 900;
  color: #000;
}

/* Action Section & Buttons */
.action-section {
  text-align: center;
  padding-top: 20px;
  border-top: 2px solid rgba(107, 114, 128, 0.1);
}

.button-group {
  display: flex;
  gap: 15px;
  justify-content: center;
  flex-wrap: wrap;
}

.btn {
  padding: 16px 32px;
  border: none;
  border-radius: 12px;
  font-size: 1em;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  cursor: pointer;
  transition: all 0.4s ease;
  position: relative;
  overflow: hidden;
  min-width: 160px;
}

.btn-content {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  position: relative;
  z-index: 2;
}

.btn-icon {
  width: 18px;
  height: 18px;
  transition: transform 0.3s ease;
}

.spinner-icon {
  animation: spin 1s linear infinite;
}

.btn-delete {
  background: linear-gradient(135deg, var(--red-accent), var(--pink-accent));
  color: var(--white);
  box-shadow: 0 10px 40px rgba(239, 68, 68, 0.4);
}

.btn-delete:hover {
  transform: translateY(-3px) scale(1.02);
  box-shadow: 0 15px 60px rgba(239, 68, 68, 0.6);
}

.btn-details {
  background: linear-gradient(135deg, var(--cyan-accent), var(--primary-blue));
  color: var(--white);
  box-shadow: 0 10px 40px rgba(6, 182, 212, 0.4);
}

.btn-details:hover {
  transform: translateY(-3px) scale(1.02);
  box-shadow: 0 15px 60px rgba(6, 182, 212, 0.6);
}

.btn-close {
  background: linear-gradient(135deg, var(--success-green), var(--accent-orange));
  color: var(--white);
  box-shadow: 0 10px 40px rgba(16, 185, 129, 0.4);
}

.btn-close:hover {
  transform: translateY(-3px) scale(1.02);
  box-shadow: 0 15px 60px rgba(16, 185, 129, 0.6);
}

.btn-shimmer {
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, 
    transparent, 
    rgba(255, 255, 255, 0.2), 
    transparent);
  transition: left 0.6s ease;
  z-index: 1;
}

.btn:hover .btn-shimmer {
  left: 100%;
}

.btn:hover .btn-icon {
  transform: scale(1.1);
}

.btn:disabled {
  opacity: 0.7;
  cursor: not-allowed;
  animation: none;
}

.btn:focus {
  outline: 3px solid var(--accent-orange);
  outline-offset: 2px;
}

/* Floating Decorative Elements */
.floating-elements {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
  z-index: 0;
}

.float-shape {
  position: absolute;
  border-radius: 50%;
  opacity: 0.08;
}

.shape-1 {
  width: 120px;
  height: 120px;
  top: 5%;
  right: 5%;
  background: linear-gradient(135deg, var(--success-green), var(--cyan-accent));
  animation: floatAround 12s ease-in-out infinite;
}

.shape-2 {
  width: 80px;
  height: 80px;
  bottom: 10%;
  left: 8%;
  background: linear-gradient(135deg, var(--accent-orange), var(--pink-accent));
  animation: floatAround 8s ease-in-out infinite reverse;
}

.shape-3 {
  width: 100px;
  height: 100px;
  top: 40%;
  right: 15%;
  background: linear-gradient(135deg, var(--accent-purple), var(--primary-blue));
  animation: floatAround 15s ease-in-out infinite;
}

@keyframes floatAround {
  0%, 100% { transform: translate(0, 0) rotate(0deg); }
  25% { transform: translate(20px, -20px) rotate(90deg); }
  50% { transform: translate(-15px, -30px) rotate(180deg); }
  75% { transform: translate(-25px, 15px) rotate(270deg); }
}

/* Animations */
.details-section {
  animation: fadeInUp 0.8s ease-out 0.2s both;
}

@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

/* Responsive Design */
@media (max-width: 768px) {
  .edit-container {
    padding: 40px 25px;
    margin: 10px;
  }
  
  .page-title {
    font-size: 2em;
  }
  
  .details-grid {
    grid-template-columns: 1fr;
    gap: 15px;
  }
  
  .button-group {
    flex-direction: column;
    align-items: center;
  }
  
  .btn {
    width: 100%;
    max-width: 280px;
  }
}

@media (max-width: 480px) {
  .edit-container {
    padding: 30px 20px;
  }
  
  .page-title {
    font-size: 1.8em;
  }
  
  .parking-icon .icon {
    width: 50px;
    height: 50px;
  }
  
  .detail-item {
    padding: 15px;
  }
  
  .item-icon {
    font-size: 1.5em;
    padding: 8px;
    min-width: 40px;
    height: 40px;
  }
}
</style>