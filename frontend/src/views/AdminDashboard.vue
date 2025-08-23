<template>
  <div class="admin-dashboard">
    <!-- Background Pattern -->
    <div class="bg-pattern"></div>
    
    <!-- Navigation Bar -->
    <nav class="main-nav">
      <div class="nav-container">
        <div class="nav-brand">
          <svg viewBox="0 0 100 100" class="brand-icon">
            <rect x="10" y="20" width="80" height="60" rx="5" fill="none" stroke="currentColor" stroke-width="3"/>
            <rect x="20" y="30" width="15" height="25" rx="2" fill="currentColor"/>
            <rect x="42.5" y="30" width="15" height="25" rx="2" fill="currentColor"/>
            <rect x="65" y="30" width="15" height="25" rx="2" fill="currentColor"/>
            <text x="50" y="70" text-anchor="middle" font-size="12" fill="currentColor" font-weight="bold">P</text>
          </svg>
          <span class="brand-text">ParkSmart Admin</span>
        </div>
        
        <div class="nav-links">
          <router-link to="/admin-dashboard" class="nav-link home-link">
            <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
              <polyline points="9,22 9,12 15,12 15,22"/>
            </svg>
            Home
          </router-link>
          
          <router-link to="/user-stat" class="nav-link users-link">
            <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/>
              <circle cx="9" cy="7" r="4"/>
              <path d="M23 21v-2a4 4 0 0 0-3-3.87"/>
              <path d="M16 3.13a4 4 0 0 1 0 7.75"/>
            </svg>
            Users
          </router-link>
          
          <router-link to="/search" class="nav-link search-link">
            <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <circle cx="11" cy="11" r="8"/>
              <path d="M21 21l-4.35-4.35"/>
            </svg>
            Search
          </router-link>
          
          <router-link to="/admin-summary" class="nav-link summary-link">
            <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M9 11H5a2 2 0 0 0-2 2v7a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7a2 2 0 0 0-2-2h-4"/>
              <polyline points="6,9 12,15 18,9"/>
            </svg>
            Summary
          </router-link>
          
          <router-link to="/" class="nav-link logout-link">
            <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"/>
              <polyline points="16,17 21,12 16,7"/>
              <line x1="21" y1="12" x2="9" y2="12"/>
            </svg>
            Logout
          </router-link>
        </div>
      </div>
    </nav>

    <!-- Main Content -->
    <div class="main-content">
      <router-view/>
      
      <!-- Dashboard Content -->
      <div class="dashboard-container">
        <!-- Header Section -->
        <div class="content-header">
          <div class="header-content">
            <h1 class="dashboard-title">
              <span class="gradient-text">Parking Lots Management</span>
            </h1>
            <router-link to="/add-lot" class="btn btn-add-lot">
              <span class="btn-content">
                <svg class="btn-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <line x1="12" y1="5" x2="12" y2="19"/>
                  <line x1="5" y1="12" x2="19" y2="12"/>
                </svg>
                Add New Lot
              </span>
              <div class="btn-shimmer"></div>
            </router-link>
          </div>
        </div>

        <!-- Parking Lots Grid -->
        <div class="lots-grid">
          <div v-for="lot in parkingLots" :key="lot.id" class="lot-card">
            <!-- Lot Card Header -->
            <div class="lot-header">
              <div class="lot-info">
                <h3 class="lot-name">{{ lot.prime_location_name }}</h3>
                <p class="lot-address">
                  <svg class="address-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
                    <circle cx="12" cy="10" r="3"/>
                  </svg>
                  {{ lot.address }}
                </p>
              </div>
              
              <div class="lot-actions">
                <button class="action-btn edit-btn" @click="editLot(lot.id)">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M11 4H4a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7"/>
                    <path d="M18.5 2.5a2.121 2.121 0 0 1 3 3L12 15l-4 1 1-4 9.5-9.5z"/>
                  </svg>
                </button>
                <button class="action-btn delete-btn" @click="deleteLot(lot.id)">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <polyline points="3,6 5,6 21,6"/>
                    <path d="M19,6v14a2,2 0 0,1 -2,2H7a2,2 0 0,1 -2,-2V6m3,0V4a2,2 0 0,1 2,-2h4a2,2 0 0,1 2,2v2"/>
                    <line x1="10" y1="11" x2="10" y2="17"/>
                    <line x1="14" y1="11" x2="14" y2="17"/>
                  </svg>
                </button>
              </div>
            </div>

            <!-- Occupancy Stats -->
            <div class="occupancy-stats">
              <div class="stat-item occupied-stat">
                <div class="stat-icon">🚗</div>
                <div class="stat-content">
                  <span class="stat-number">{{ lot.occupiedCount }}</span>
                  <span class="stat-label">Occupied</span>
                </div>
              </div>
              
              <div class="stat-divider"></div>
              
              <div class="stat-item available-stat">
                <div class="stat-icon">🅿️</div>
                <div class="stat-content">
                  <span class="stat-number">{{ lot.number_of_spots - lot.occupiedCount }}</span>
                  <span class="stat-label">Available</span>
                </div>
              </div>
              
              <div class="stat-divider"></div>
              
              <div class="stat-item total-stat">
                <div class="stat-icon">📊</div>
                <div class="stat-content">
                  <span class="stat-number">{{ lot.number_of_spots }}</span>
                  <span class="stat-label">Total</span>
                </div>
              </div>
            </div>

            <!-- Occupancy Progress Bar -->
            <div class="progress-container">
              <div class="progress-bar">
                <div 
                  class="progress-fill" 
                  :style="{ width: (lot.occupiedCount / lot.number_of_spots * 100) + '%' }"
                ></div>
              </div>
              <span class="progress-text">
                {{ Math.round(lot.occupiedCount / lot.number_of_spots * 100) }}% Occupied
              </span>
            </div>

            <!-- Spots Grid -->
            <div class="spots-section">
              <h4 class="spots-title">Parking Spots</h4>
              <div class="spots-grid">
                <button 
                  v-for="n in lot.number_of_spots"
                  :key="`${lot.id}-${n}`"
                  class="spot-button"
                  :class="[
                    getSpotStatus(lot, n) === 'A' ? 'spot-available' : 'spot-occupied',
                    `spot-${n % 4 + 1}`
                  ]"
                  @click="goToEditSpot(lot, n)"
                >
                  <div class="spot-number">{{ n }}</div>
                  <div class="spot-status">{{ getSpotStatus(lot, n) === 'A' ? 'Free' : 'Busy' }}</div>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Floating Action Elements -->
    <div class="floating-elements">
      <div class="float-shape shape-1"></div>
      <div class="float-shape shape-2"></div>
      <div class="float-shape shape-3"></div>
      <div class="float-shape shape-4"></div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      parkingLots: [],
      currentUserId: 1 // Ensure this is set from your auth logic
    };
  },
  mounted() {
    this.fetchLots();
  },
  methods: {
    editLot(lotId) {
      this.$router.push({ name: 'EditLot', params: { id: lotId } });
    },

    async deleteLot(lotId) {
      if (!confirm('Are you sure you want to delete this lot?')) return;
      try {
        const res = await fetch(`http://localhost:5000/api/parkinglot`, {
          method: 'DELETE',
          headers: {'Content-Type':'application/json'},
          body: JSON.stringify({ id: lotId })
        });
        const json = await res.json();
        if (json.status === 'ok') {
            this.parkingLots = this.parkingLots.filter(lot => lot.id !== lotId);
            await this.fetchLots();
            alert('Parking lot deleted successfully!');
        } else {
          alert(`Delete failed: ${json.message}`);
        }
      } catch (e) {
        console.error(e);
      }
    },

    async fetchLots() {
      const res = await fetch("http://localhost:5000/api/parkinglot");
      if (!res.ok) return console.error("Failed to load lots");

      const data = await res.json();
      this.parkingLots = data.lots.map(lot => {
        const spots = lot.spots || [];
        const occupiedCount = spots.filter(s => s.status === 'O').length;
        const availableCount = spots.filter(s => s.status === 'A').length;

        return {
          ...lot,
          occupiedCount,
          availableCount,
          spots,  // keep for button display
        };
      });
    },

    getSpotStatus(lot, n) {
      const spot = lot.spots.find(s => s.spot_number === `Spot-${n}`);
      return spot ? spot.status : 'A';  // default to 'A' if not found
    },
    
    goToEditSpot(lot, n) {
      this.$router.push({ 
        name: 'editspot',
        params: { lotId : lot.id, spotNum : n} 
      })
    },
  }
};
</script>

<style scoped>
/* Color Variables - Vibrant Parking Theme */
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

.admin-dashboard {
  min-height: 100vh;
  background: linear-gradient(135deg, 
    var(--dark-gray) 0%, 
    var(--primary-blue) 25%, 
    var(--accent-purple) 50%, 
    var(--pink-accent) 75%, 
    var(--accent-orange) 100%);
  background-size: 400% 400%;
  animation: gradientShift 15s ease infinite;
  position: relative;
  overflow-x: hidden;
}

@keyframes gradientShift {
  0% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
  100% { background-position: 0% 50%; }
}

/* Animated Background Pattern */
.bg-pattern {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: 
    radial-gradient(circle at 20% 20%, rgba(255, 255, 255, 0.05) 0%, transparent 50%),
    radial-gradient(circle at 80% 80%, rgba(245, 158, 11, 0.05) 0%, transparent 50%),
    radial-gradient(circle at 60% 40%, rgba(139, 92, 246, 0.05) 0%, transparent 50%),
    repeating-linear-gradient(
      45deg,
      transparent,
      transparent 120px,
      rgba(255, 255, 255, 0.01) 122px,
      rgba(255, 255, 255, 0.01) 124px
    );
  animation: drift 30s linear infinite, pulse 10s ease-in-out infinite;
  z-index: 0;
}

@keyframes drift {
  0% { transform: translate(0, 0) rotate(0deg); }
  100% { transform: translate(100px, 100px) rotate(360deg); }
}

@keyframes pulse {
  0%, 100% { opacity: 0.4; }
  50% { opacity: 0.8; }
}

/* Navigation Bar */
.main-nav {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border-bottom: 2px solid transparent;
  background-image: linear-gradient(rgba(255, 255, 255, 0.95), rgba(255, 255, 255, 0.95)),
                    linear-gradient(90deg, var(--success-green), var(--cyan-accent), var(--accent-orange));
  background-origin: border-box;
  background-clip: content-box, border-box;
  padding: 15px 0;
  position: sticky;
  top: 0;
  z-index: 100;
  box-shadow: 0 8px 32px var(--shadow);
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 20px;
}

.nav-brand {
  display: flex;
  align-items: center;
  gap: 12px;
}

.brand-icon {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, var(--primary-blue), var(--accent-purple));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: brandPulse 4s ease-in-out infinite;
}

@keyframes brandPulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.05); }
}

.brand-text {
  font-size: 1.8em;
  font-weight: 800;
  background: linear-gradient(135deg, var(--primary-blue), var(--accent-purple));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  background-color: black;
}

.nav-links {
  display: flex;
  gap: 8px;
  align-items: center;
}

.nav-link {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 20px;
  text-decoration: none;
  color: var(--medium-gray);
  font-weight: 600;
  border-radius: 12px;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.nav-icon {
  width: 18px;
  height: 18px;
}

.nav-link:hover {
  color: var(--white);
  transform: translateY(-2px);
}

.home-link:hover { background: linear-gradient(135deg, var(--primary-blue), var(--secondary-blue)); }
.users-link:hover { background: linear-gradient(135deg, var(--accent-purple), var(--pink-accent)); }
.search-link:hover { background: linear-gradient(135deg, var(--cyan-accent), var(--success-green)); }
.summary-link:hover { background: linear-gradient(135deg, var(--accent-orange), var(--pink-accent)); }
.logout-link:hover { background: linear-gradient(135deg, var(--red-accent), var(--pink-accent)); }

.nav-link.router-link-exact-active {
  background: linear-gradient(135deg, var(--primary-blue), var(--accent-purple));
  color: var(--white);
  box-shadow: 0 4px 15px rgba(37, 99, 235, 0.3);
}

/* Main Content */
.main-content {
  position: relative;
  z-index: 1;
  padding: 40px 20px;
}

.dashboard-container {
  max-width: 1200px;
  margin: 0 auto;
}

/* Content Header */
.content-header {
  margin-bottom: 40px;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 20px;
  background: rgba(255, 255, 255, 0.9);
  backdrop-filter: blur(15px);
  padding: 30px;
  border-radius: 20px;
  box-shadow: 0 15px 50px var(--shadow);
  border: 2px solid transparent;
  background-clip: padding-box;
}

.header-content::before {
  content: '';
  position: absolute;
  inset: 0;
  padding: 2px;
  background: linear-gradient(135deg, var(--success-green), var(--cyan-accent), var(--accent-orange));
  border-radius: inherit;
  mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  mask-composite: exclude;
  -webkit-mask-composite: xor;
}

.dashboard-title {
  font-size: 2.5em;
  font-weight: 800;
  margin: 0;
  letter-spacing: -1px;
}

.gradient-text {
  color: #000;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
}

@keyframes textShimmer {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}

.btn-add-lot {
  background: linear-gradient(135deg, var(--success-green), var(--cyan-accent));
  color: var(--white);
  padding: 16px 24px;
  border: none;
  border-radius: 12px;
  font-weight: 700;
  text-decoration: none;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
  box-shadow: 0 8px 32px rgba(16, 185, 129, 0.3);
}

.btn-add-lot:hover {
  transform: translateY(-3px) scale(1.05);
  box-shadow: 0 15px 60px rgba(16, 185, 129, 0.5);
  color: var(--white);
}

/* Lots Grid */
.lots-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
  gap: 30px;
}

.lot-card {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(15px);
  border-radius: 20px;
  padding: 30px;
  box-shadow: 0 20px 60px var(--shadow-dark);
  border: 2px solid transparent;
  background-clip: padding-box;
  transition: all 0.4s ease;
  position: relative;
  overflow: hidden;
  animation: cardSlideIn 0.6s ease-out;
}

@keyframes cardSlideIn {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.lot-card::before {
  content: '';
  position: absolute;
  inset: 0;
  padding: 2px;
  background: linear-gradient(135deg, 
    var(--primary-blue), 
    var(--accent-purple), 
    var(--pink-accent), 
    var(--cyan-accent));
  background-size: 400% 400%;
  border-radius: inherit;
  mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  mask-composite: exclude;
  -webkit-mask-composite: xor;
  animation: borderFlow 8s ease infinite;
}

@keyframes borderFlow {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}

.lot-card:hover {
  transform: translateY(-8px) scale(1.02);
  box-shadow: 0 30px 80px var(--shadow-dark);
}

/* Lot Header */
.lot-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 25px;
  padding-bottom: 20px;
  border-bottom: 2px solid var(--light-gray);
}

.lot-name {
  font-size: 1.4em;
  font-weight: 700;
  color: var(--dark-gray);
  margin: 0 0 8px 0;
}

.lot-address {
  display: flex;
  align-items: center;
  gap: 6px;
  color: var(--medium-gray);
  margin: 0;
  font-size: 0.95em;
  font-weight: 500;
}

.address-icon {
  width: 16px;
  height: 16px;
  color: var(--accent-orange);
}

.lot-actions {
  display: flex;
  gap: 10px;
}

.action-btn {
  width: 40px;
  height: 40px;
  border: none;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.action-btn svg {
  width: 18px;
  height: 18px;
  position: relative;
  z-index: 2;
}

.edit-btn {
  background: linear-gradient(135deg, var(--cyan-accent), var(--success-green));
  color: var(--white);
  box-shadow: 0 4px 15px rgba(6, 182, 212, 0.3);
}

.edit-btn:hover {
  transform: scale(1.1);
  box-shadow: 0 8px 25px rgba(6, 182, 212, 0.5);
}

.delete-btn {
  background: linear-gradient(135deg, var(--red-accent), var(--pink-accent));
  color: var(--white);
  box-shadow: 0 4px 15px rgba(239, 68, 68, 0.3);
}

.delete-btn:hover {
  transform: scale(1.1);
  box-shadow: 0 8px 25px rgba(239, 68, 68, 0.5);
}

/* Occupancy Stats */
.occupancy-stats {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 25px;
  background: linear-gradient(135deg, rgba(243, 244, 246, 0.5), rgba(255, 255, 255, 0.5));
  padding: 20px;
  border-radius: 16px;
  border: 1px solid rgba(255, 255, 255, 0.3);
}

.stat-item {
  display: flex;
  align-items: center;
  gap: 12px;
  flex: 1;
}

.stat-icon {
  font-size: 1.8em;
  padding: 8px;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.occupied-stat .stat-icon {
  background: linear-gradient(135deg, var(--red-accent), var(--pink-accent));
}

.available-stat .stat-icon {
  background: linear-gradient(135deg, var(--success-green), var(--cyan-accent));
}

.total-stat .stat-icon {
  background: linear-gradient(135deg, var(--primary-blue), var(--accent-purple));
}

.stat-content {
  display: flex;
  flex-direction: column;
}

.stat-number {
  font-size: 1.5em;
  font-weight: 800;
  color: var(--dark-gray);
}

.stat-label {
  font-size: 0.8em;
  color: var(--medium-gray);
  font-weight: 600;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.stat-divider {
  width: 2px;
  height: 40px;
  background: linear-gradient(to bottom, var(--light-gray), var(--medium-gray), var(--light-gray));
  border-radius: 1px;
}

/* Progress Bar */
.progress-container {
  margin-bottom: 25px;
}

.progress-bar {
  width: 100%;
  height: 8px;
  background: var(--light-gray);
  border-radius: 4px;
  overflow: hidden;
  box-shadow: inset 0 2px 4px var(--shadow);
}

.progress-fill {
  height: 100%;
  background: linear-gradient(90deg, var(--success-green), var(--cyan-accent), var(--accent-orange));
  border-radius: 4px;
  transition: width 0.6s ease;
  position: relative;
}

.progress-fill::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
  animation: progressShimmer 2s ease-in-out infinite;
}

@keyframes progressShimmer {
  0% { transform: translateX(-100%); }
  100% { transform: translateX(100%); }
}

.progress-text {
  display: block;
  text-align: center;
  margin-top: 8px;
  font-size: 0.9em;
  font-weight: 600;
  color: var(--medium-gray);
}

/* Spots Section */
.spots-section {
  margin-top: 25px;
}

.spots-title {
  font-size: 1.2em;
  font-weight: 700;
  color: var(--dark-gray);
  margin-bottom: 15px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.spots-title::before {
  content: '🅿️';
  font-size: 1.1em;
}

.spots-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(80px, 1fr));
  gap: 12px;
  max-height: 200px;
  overflow-y: auto;
  padding: 15px;
  background: rgba(243, 244, 246, 0.3);
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.2);
}

.spot-button {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  padding: 12px 8px;
  border: 2px solid transparent;
  border-radius: 10px;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
  min-height: 70px;
  font-weight: 600;
}

.spot-number {
  font-size: 1.1em;
  font-weight: 800;
  margin-bottom: 2px;
}

.spot-status {
  font-size: 0.7em;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-weight: 600;
}

/* Spot Status Colors */
.spot-available {
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(6, 182, 212, 0.1));
  border-color: var(--success-green);
  color: var(--success-green);
  box-shadow: 0 4px 15px rgba(16, 185, 129, 0.2);
}

.spot-available:hover {
  background: linear-gradient(135deg, var(--success-green), var(--cyan-accent));
  color: var(--white);
  transform: translateY(-3px) scale(1.05);
  box-shadow: 0 8px 25px rgba(16, 185, 129, 0.4);
}

.spot-occupied {
  background: linear-gradient(135deg, rgba(239, 68, 68, 0.1), rgba(236, 72, 153, 0.1));
  border-color: var(--red-accent);
  color: var(--red-accent);
  box-shadow: 0 4px 15px rgba(239, 68, 68, 0.2);
}

.spot-occupied:hover {
  background: linear-gradient(135deg, var(--red-accent), var(--pink-accent));
  color: var(--white);
  transform: translateY(-3px) scale(1.05);
  box-shadow: 0 8px 25px rgba(239, 68, 68, 0.4);
}

/* Spot Animation Variants */
.spot-1:hover { animation: bounceRotate 0.6s ease; }
.spot-2:hover { animation: pulse 0.6s ease; }
.spot-3:hover { animation: wiggle 0.6s ease; }
.spot-4:hover { animation: glow 0.6s ease; }

@keyframes bounceRotate {
  0%, 100% { transform: translateY(-3px) scale(1.05) rotate(0deg); }
  50% { transform: translateY(-6px) scale(1.1) rotate(5deg); }
}

@keyframes wiggle {
  0%, 100% { transform: translateY(-3px) scale(1.05) rotate(0deg); }
  25% { transform: translateY(-3px) scale(1.05) rotate(-2deg); }
  75% { transform: translateY(-3px) scale(1.05) rotate(2deg); }
}

@keyframes glow {
  0%, 100% { transform: translateY(-3px) scale(1.05); filter: brightness(1); }
  50% { transform: translateY(-6px) scale(1.1); filter: brightness(1.2); }
}

/* Button Styling */
.btn-content {
  display: flex;
  align-items: center;
  gap: 8px;
  position: relative;
  z-index: 2;
}

.btn-icon {
  width: 18px;
  height: 18px;
  transition: transform 0.3s ease;
}

.btn-shimmer {
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, 
    transparent, 
    rgba(255, 255, 255, 0.3), 
    transparent);
  transition: left 0.6s ease;
  z-index: 1;
}

.btn-add-lot:hover .btn-shimmer {
  left: 100%;
}

.btn-add-lot:hover .btn-icon {
  transform: rotate(90deg);
}

/* Floating Decorative Elements */
.floating-elements {
  position: fixed;
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
  opacity: 0.05;
}

.shape-1 {
  width: 150px;
  height: 150px;
  top: 10%;
  right: 5%;
  background: linear-gradient(135deg, var(--success-green), var(--cyan-accent));
  animation: floatAround 20s ease-in-out infinite;
}

.shape-2 {
  width: 100px;
  height: 100px;
  bottom: 20%;
  left: 10%;
  background: linear-gradient(135deg, var(--accent-orange), var(--pink-accent));
  animation: floatAround 15s ease-in-out infinite reverse;
}

.shape-3 {
  width: 120px;
  height: 120px;
  top: 50%;
  right: 20%;
  background: linear-gradient(135deg, var(--accent-purple), var(--primary-blue));
  animation: floatAround 18s ease-in-out infinite;
}

.shape-4 {
  width: 80px;
  height: 80px;
  top: 30%;
  left: 15%;
  background: linear-gradient(135deg, var(--pink-accent), var(--cyan-accent));
  animation: floatAround 12s ease-in-out infinite reverse;
}

@keyframes floatAround {
  0%, 100% { transform: translate(0, 0) rotate(0deg); }
  25% { transform: translate(30px, -25px) rotate(90deg); }
  50% { transform: translate(-20px, -40px) rotate(180deg); }
  75% { transform: translate(-35px, 20px) rotate(270deg); }
}

/* Responsive Design */
@media (max-width: 1024px) {
  .lots-grid {
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 25px;
  }
  
  .header-content {
    flex-direction: column;
    text-align: center;
  }
  
  .dashboard-title {
    font-size: 2.2em;
  }
}

@media (max-width: 768px) {
  .nav-links {
    flex-wrap: wrap;
    gap: 5px;
  }
  
  .nav-link {
    padding: 10px 15px;
    font-size: 0.9em;
  }
  
  .lots-grid {
    grid-template-columns: 1fr;
    gap: 20px;
  }
  
  .lot-card {
    padding: 25px 20px;
  }
  
  .dashboard-title {
    font-size: 1.8em;
  }
  
  .occupancy-stats {
    flex-direction: column;
    gap: 15px;
  }
  
  .stat-divider {
    width: 100%;
    height: 2px;
  }
  
  .spots-grid {
    grid-template-columns: repeat(auto-fit, minmax(70px, 1fr));
    gap: 8px;
  }
}

@media (max-width: 480px) {
  .main-content {
    padding: 20px 10px;
  }
  
  .nav-container {
    flex-direction: column;
    gap: 15px;
    padding: 0 15px;
  }
  
  .nav-links {
    justify-content: center;
  }
  
  .dashboard-title {
    font-size: 1.6em;
  }
  
  .lot-header {
    flex-direction: column;
    gap: 15px;
    align-items: center;
    text-align: center;
  }
  
  .spot-button {
    min-height: 60px;
    padding: 8px 6px;
  }
  
  .spots-grid {
    max-height: 150px;
  }
}

/* Focus States for Accessibility */
.action-btn:focus,
.spot-button:focus,
.nav-link:focus {
  outline: 3px solid var(--accent-orange);
  outline-offset: 2px;
}

/* Loading States */
.lot-card.loading {
  opacity: 0.7;
  pointer-events: none;
}

/* Enhanced Interactions */
.lot-card:hover .lot-name {
  background: linear-gradient(135deg, var(--primary-blue), var(--accent-purple));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  transition: all 0.3s ease;
}

.occupancy-stats:hover {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.7), rgba(243, 244, 246, 0.7));
  transform: scale(1.02);
  transition: all 0.3s ease;
}

/* Custom Scrollbar for Spots Grid */
.spots-grid::-webkit-scrollbar {
  width: 6px;
}

.spots-grid::-webkit-scrollbar-track {
  background: rgba(243, 244, 246, 0.5);
  border-radius: 3px;
}

.spots-grid::-webkit-scrollbar-thumb {
  background: linear-gradient(to bottom, var(--primary-blue), var(--accent-purple));
  border-radius: 3px;
}

.spots-grid::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(to bottom, var(--accent-purple), var(--pink-accent));
}
</style>