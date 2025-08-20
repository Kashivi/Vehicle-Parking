<template>
  <div class="user-dashboard">
    <!-- Animated Background -->
    <div class="bg-pattern"></div>
    
    <!-- Navigation Header -->
    <nav class="navbar">
      <div class="nav-container">
        <div class="nav-brand">
          <div class="parking-icon">
            <svg viewBox="0 0 100 100" class="icon">
              <rect x="10" y="20" width="80" height="60" rx="5" fill="none" stroke="currentColor" stroke-width="3"/>
              <rect x="20" y="30" width="15" height="25" rx="2" fill="currentColor"/>
              <rect x="42.5" y="30" width="15" height="25" rx="2" fill="currentColor"/>
              <rect x="65" y="30" width="15" height="25" rx="2" fill="currentColor"/>
              <text x="50" y="70" text-anchor="middle" font-size="12" fill="currentColor" font-weight="bold">P</text>
            </svg>
          </div>
          <span class="brand-text">ParkSmart</span>
        </div>
        
        <div class="nav-links">
          <router-link to="/user-dashboard" class="nav-link active">
            <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/>
            </svg>
            Home
          </router-link>
          <router-link to="/user-summary" class="nav-link">
            <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M9 11H5a2 2 0 0 0-2 2v7a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7a2 2 0 0 0-2-2h-4"/>
              <path d="M9 11V9a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2"/>
            </svg>
            Summary
          </router-link>
          <router-link to="/edituser" class="nav-link">
            <svg class="nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
              <circle cx="12" cy="7" r="4"/>
            </svg>
            Profile
          </router-link>
          <router-link to="/" class="nav-link logout">
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
      
      <!-- Welcome Section -->
      <div class="welcome-section">
        <div class="welcome-content">
          <h1 class="welcome-title">
            <span class="gradient-text">Welcome back, {{username }}! 🚗</span>
          </h1>
          <p class="welcome-subtitle">Manage your parking reservations with ease</p>
        </div>
        <div class="stats-cards">
          <div class="stat-card">
            <div class="stat-icon blue">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
                <line x1="16" y1="2" x2="16" y2="6"/>
                <line x1="8" y1="2" x2="8" y2="6"/>
                <line x1="3" y1="10" x2="21" y2="10"/>
              </svg>
            </div>
            <div class="stat-content">
              <div class="stat-number">{{ activeReservationsCount }}</div>
              <div class="stat-label">Active Reservations</div>
            </div>
          </div>
        </div>
      </div>

      <!-- Recent Reservations Section -->
      <div v-if="recentReservations.length" class="section-card">
        <div class="section-header">
          <h3 class="section-title">
            <div class="title-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
                <line x1="16" y1="2" x2="16" y2="6"/>
                <line x1="8" y1="2" x2="8" y2="6"/>
                <line x1="3" y1="10" x2="21" y2="10"/>
              </svg>
            </div>
            Recent Reservations
          </h3>
          <div class="section-badge">{{ recentReservations.length }} Recent</div>
        </div>
        
        <div class="table-container">
          <table class="modern-table">
            <thead>
              <tr>
                <th>Lot ID</th>
                <th>Location</th>
                <th>Vehicle</th>
                <th>Parking Time</th>
                <th>Status</th>
                <th>Action</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="res in recentReservations" :key="res.lot_id + res.parking_timestamp" class="table-row">
                <td>
                  <div class="lot-id-badge">{{ res.lot_id }}</div>
                </td>
                <td>
                  <div class="location-cell">
                    <svg class="location-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
                      <circle cx="12" cy="10" r="3"/>
                    </svg>
                    {{ res.location }}
                  </div>
                </td>
                <td>
                  <div class="vehicle-cell">
                    <svg class="vehicle-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M7 17m-2 0a2 2 0 1 0 4 0a2 2 0 1 0 -4 0"/>
                      <path d="M17 17m-2 0a2 2 0 1 0 4 0a2 2 0 1 0 -4 0"/>
                      <path d="M5 17h-2v-6l2-5h9l4 5h1a2 2 0 0 1 2 2v4h-2"/>
                    </svg>
                    {{ res.vehicle_number }}
                  </div>
                </td>
                <td>{{ res.parking_timestamp }}</td>
                <td>
                   <span :class="['status-badge', res.is_active ? 'status-active' : 'status-completed']">
    {{ res.is_active ? 'Active' : 'Completed' }}
  </span>
                </td>
                <td>
                  <button
                     v-if="res.is_active"
    @click="goToReleasePage(res.lot_id, res.spot_id)"
    class="btn btn-release"
                  >
                    <svg class="btn-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M18 6L6 18M6 6l12 12"/>
                    </svg>
                    Release
                  </button>
                  <span v-else class="completed-text">Parked Out</span>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- Search Section -->
      <div class="section-card">
        <div class="section-header">
          <h3 class="section-title">
            <div class="title-icon">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="11" cy="11" r="8"/>
                <path d="M21 21l-4.35-4.35"/>
              </svg>
            </div>
            Find Parking Lots
          </h3>
          <div class="section-description">Discover available parking spaces near you</div>
        </div>

        <div class="search-container">
          <div class="search-controls">
            <div class="search-criterion">
              <label for="search-select" class="search-label">Search By:</label>
              <select v-model="criterion" id="search-select" class="search-select">
                <option value="location">📍 Location</option>
                <option value="pincode">📮 Pincode</option>
              </select>
            </div>

            <div class="search-input-group">
              <div class="search-input-wrapper">
                <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="11" cy="11" r="8"/>
                  <path d="M21 21l-4.35-4.35"/>
                </svg>
                <input
                  v-model="query"
                  @keyup.enter="doSearch"
                  type="text"
                  :placeholder="criterion === 'location' ? 'Enter location (e.g., Downtown, Mall Road)' : 'Enter pincode (e.g., 110001)'"
                  class="search-input"
                />
                <button type="button" @click="doSearch" class="search-btn">
                  <span class="btn-text">Search</span>
                  <div class="btn-shimmer"></div>
                </button>
              </div>
            </div>
          </div>

          <!-- Search Results -->
          <div v-if="results" class="results-section">
            <div v-if="results.lots.length" class="results-header">
              <h4 class="results-title">
                <svg class="results-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/>
                  <polyline points="3.27,6.96 12,12.01 20.73,6.96"/>
                  <line x1="12" y1="22.08" x2="12" y2="12"/>
                </svg>
                Found {{ results.lots.length }} parking lot{{ results.lots.length !== 1 ? 's' : '' }}
              </h4>
            </div>

            <div class="parking-lots-grid">
              <div v-for="lot in results.lots" :key="lot.id" class="parking-lot-card">
                <div class="lot-header">
                  <div class="lot-id">
                    <span class="lot-badge">LOT {{ lot.id }}</span>
                  </div>
                  <div class="lot-availability">
                    <div class="availability-indicator" :class="lot.availableSpots > 0 ? 'available' : 'full'">
                      <div class="indicator-dot"></div>
                      {{ lot.availableSpots > 0 ? 'Available' : 'Full' }}
                    </div>
                  </div>
                </div>
                
                <div class="lot-content">
                  <div class="lot-address">
                    <svg class="address-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
                      <circle cx="12" cy="10" r="3"/>
                    </svg>
                    {{ lot.address }}
                  </div>
                  
                  <div class="lot-details">
                    <div class="detail-item price">
                      <svg class="detail-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <line x1="12" y1="1" x2="12" y2="23"/>
                        <path d="M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/>
                      </svg>
                      <span class="price-value">₹{{ lot.price }}</span>
                      <span class="price-unit">/hour</span>
                    </div>
                    
                    <div class="detail-item spots">
                      <svg class="detail-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <rect x="3" y="4" width="18" height="18" rx="2" ry="2"/>
                        <line x1="16" y1="2" x2="16" y2="6"/>
                        <line x1="8" y1="2" x2="8" y2="6"/>
                        <line x1="3" y1="10" x2="21" y2="10"/>
                      </svg>
                      <span class="spots-available">{{ lot.availableSpots }}</span>
                      <span class="spots-total">/{{ lot.totalSpots }} spots</span>
                    </div>
                  </div>
                </div>
                
                <div class="lot-actions">
                  <router-link :to="{ path: '/book-spot', query: { lot_id: lot.id } }" class="book-link">
                    <button class="btn btn-book" :disabled="lot.availableSpots === 0">
                      <svg class="btn-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        <path d="M9 11H5a2 2 0 0 0-2 2v7a2 2 0 0 0 2 2h14a2 2 0 0 0 2-2v-7a2 2 0 0 0-2-2h-4"/>
                        <path d="M9 11V9a2 2 0 0 1 2-2h2a2 2 0 0 1 2 2v2"/>
                      </svg>
                      <span class="btn-text">{{ lot.availableSpots === 0 ? 'Full' : 'Book Now' }}</span>
                      <div class="btn-shimmer"></div>
                    </button>
                  </router-link>
                </div>
              </div>
            </div>

            <div v-if="!results.lots.length" class="no-results">
              <div class="no-results-icon">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="11" cy="11" r="8"/>
                  <path d="M21 21l-4.35-4.35"/>
                </svg>
              </div>
              <h4>No parking lots found</h4>
              <p>Try searching with a different location or pincode</p>
            </div>
          </div>
        </div>
      </div>

      <!-- Floating Action Shapes -->
      <div class="floating-shapes">
        <div class="shape shape-1"></div>
        <div class="shape shape-2"></div>
        <div class="shape shape-3"></div>
        <div class="shape shape-4"></div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'UserDashboard',
  data() {
    return {
      criterion: 'location',
      query: '',
      results: null,
      username: '',
      token: localStorage.getItem('auth_token') || '',
      recentReservations: [],
      activeReservationsCount: 0
    };
  },
  mounted() {
    const lotId = this.$route.params.lot_id;
    const spotId = this.$route.params.spot_id;
    console.log('Navigated to release:', lotId, spotId);
    this.token = localStorage.getItem('auth_token') || ''
    const stored = localStorage.getItem('user');
    if (stored) {
      try {
        this.username = JSON.parse(stored).username || stored;
      } catch {
        this.username = stored;
      }
    }
    this.fetchRecentReservations(); // fetch anyway
    this.fetchActiveReservationsCount();

    // If user just returned from releasing
    if (this.$route.query.refresh === 'true') {
      console.log("🔁 Refreshing dashboard after release...");
      this.fetchRecentReservations();
      this.fetchActiveReservationsCount();
      this.$router.replace({ query: {} });  // Clears URL query after reload
    }
  },
  methods: {
    logout() {
      localStorage.removeItem('user');
      this.$router.push({ name: 'Login' });
    },
    
    async fetchActiveReservationsCount() {
      const config = { 
        headers: { 
          'Authorization': this.token,
          'Content-Type': 'application/json'
        } 
      };
      
      try {
        console.log("Fetching active reservations count...");
        const resp = await axios.get(
          `http://localhost:5000/api/active-reservations-count`, 
          config
        );
        
        console.log('Active count response:', resp.data);
        
        if (resp.data && typeof resp.data.active_count === 'number') {
          this.activeReservationsCount = resp.data.active_count;
        } else {
          // Fallback: count active reservations from recent list
          this.activeReservationsCount = this.recentReservations.filter(
            res => res.is_active
          ).length;
        }
      }catch (err) {
        console.error('Error loading active reservations count:', err);
        
        // Fallback: count active reservations from recent list
        this.activeReservationsCount = this.recentReservations.filter(
          res => !res.leaving_timestamp && res.reservation_status !== 'Parked Out'
        ).length;
      }
    },

    async fetchRecentReservations() {
      const config = { headers: { 'Authorization': this.token } };
      try {
        const resp = await axios.get(`http://localhost:5000/api/recent-reservations`, config);
        console.log('Fetched recent:', resp.data.recent); 
        this.recentReservations = resp.data.recent || [];
      } 
      catch (err) {
        console.error('Error loading recent reservations:', err);
      }
    },

    goToReleasePage(lotId, spotId) {
      const user = JSON.parse(localStorage.getItem('user') || '{}');
      const userId = user.user_id;

      this.$router.push({
        name: 'ReleaseSpot',
        query: {
          lot_id: lotId,
          spot_id: spotId,
          user_id: userId
        }
      });
    },

    async doSearch() {
      const config = { headers: { 'Authorization': this.token } };

      try {
        const resp = await axios.get(`http://localhost:5000/api/parkinglot`, {
          params: {
            query: this.criterion === 'location' ? this.query : undefined,
            pincode: this.criterion === 'pincode' ? this.query : undefined
          },
          ...config
        });
        const lots = resp.data.lots || [];
        this.results = {
          lots: lots.map(lot => {
            const spots = Array.isArray(lot.spots) ? lot.spots : [];
            const occupiedCount = spots.filter(s => s.status === 'O').length;
            return {
              id: lot.id,
              address: lot.address,
              price: lot.price,
              totalSpots: lot.number_of_spots,
              availableSpots: lot.available_spots,
              spots
            };
          })
        };
      } catch (err) {
        if (err.response && err.response.status === 404) {
          this.results = { lots: [] };
        } else {
          console.error('Search error:', err);
        }
      }
    },
  }
};
</script>

<style scoped>
/* Color Variables - Parking Theme */
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

.user-dashboard {
  min-height: 100vh;
  background: linear-gradient(135deg, 
    var(--primary-blue) 0%, 
    var(--accent-purple) 25%, 
    var(--pink-accent) 50%, 
    var(--cyan-accent) 75%, 
    var(--success-green) 100%);
  background-size: 400% 400%;
  animation: gradientShift 15s ease infinite;
  position: relative;
  padding-bottom: 40px;
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
    radial-gradient(circle at 20% 30%, rgba(255, 255, 255, 0.1) 0%, transparent 50%),
    radial-gradient(circle at 80% 70%, rgba(245, 158, 11, 0.1) 0%, transparent 50%),
    radial-gradient(circle at 60% 20%, rgba(139, 92, 246, 0.1) 0%, transparent 50%),
    repeating-linear-gradient(
      45deg,
      transparent,
      transparent 80px,
      rgba(255, 255, 255, 0.02) 82px,
      rgba(255, 255, 255, 0.02) 84px
    );
  animation: drift 25s linear infinite;
  pointer-events: none;
}

@keyframes drift {
  0% { transform: translate(0, 0) rotate(0deg); }
  100% { transform: translate(50px, 50px) rotate(360deg); }
}

/* Navigation */
.navbar {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
  padding: 20px 0;
  position: sticky;
  top: 0;
  z-index: 100;
  animation: slideDown 0.8s ease-out;
}

@keyframes slideDown {
  from {
    opacity: 0;
    transform: translateY(-100px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 30px;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-brand {
  display: flex;
  align-items: center;
  gap: 15px;
}

.parking-icon {
  background: linear-gradient(135deg, var(--cyan-accent), var(--primary-blue), var(--accent-purple));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  animation: float 3s ease-in-out infinite;
}

.parking-icon .icon {
  width: 40px;
  height: 40px;
}

@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-5px); }
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
}

.nav-link {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 12px 20px;
  border-radius: 12px;
  text-decoration: none;
  color: var(--medium-gray);
  font-weight: 600;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.nav-link:hover {
  background: linear-gradient(135deg, rgba(37, 99, 235, 0.1), rgba(139, 92, 246, 0.1));
  color: var(--primary-blue);
  transform: translateY(-2px);
}

.nav-link.active {
  background: linear-gradient(135deg, var(--primary-blue), var(--accent-purple));
  color: var(--white);
  box-shadow: 0 8px 25px rgba(37, 99, 235, 0.3);
}

.nav-link.logout:hover {
  background: linear-gradient(135deg, rgba(239, 68, 68, 0.1), rgba(236, 72, 153, 0.1));
  color: var(--red-accent);
}

.nav-icon {
  width: 18px;
  height: 18px;
}

/* Main Content */
.main-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 40px 30px;
  position: relative;
  z-index: 1;
}

/* Welcome Section */
.welcome-section {
  text-align: center;
  margin-bottom: 50px;
  animation: fadeInUp 0.8s ease-out;
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

.welcome-content {
  margin-bottom: 30px;
}

.welcome-title {
  font-size: 3em;
  font-weight: 800;
  margin-bottom: 15px;
  letter-spacing: -1px;
}

.gradient-text {
  color: #000;
  text-shadow: 0 1px 3px rgba(0, 0, 0, 0.2);
}


@keyframes textGlow {
  0%, 100% { filter: drop-shadow(0 0 20px rgba(255, 255, 255, 0.5)); }
  50% { filter: drop-shadow(0 0 30px rgba(255, 255, 255, 0.8)); }
}

.welcome-subtitle {
  color: rgb(0, 0, 0);
  font-size: 1.2em;
  font-weight: 500;
}

/* Stats Cards */
.stats-cards {
  display: flex;
  justify-content: center;
  gap: 20px;
}

.stat-card {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(15px);
  border-radius: 20px;
  padding: 25px;
  display: flex;
  align-items: center;
  gap: 20px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 10px 40px var(--shadow-dark);
  animation: cardFloat 4s ease-in-out infinite;
}

@keyframes cardFloat {
  0%, 100% { transform: translateY(0px) rotate(0deg); }
  50% { transform: translateY(-8px) rotate(1deg); }
}

.stat-icon {
  width: 50px;
  height: 50px;
  border-radius: 15px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--white);
}

.stat-icon.blue {
  background: linear-gradient(135deg, var(--primary-blue), var(--cyan-accent));
}

.stat-icon svg {
  width: 24px;
  height: 24px;
}

.stat-number {
  font-size: 2em;
  font-weight: 800;
  color: var(--dark-gray);
}

.stat-label {
  color: var(--medium-gray);
  font-weight: 600;
  font-size: 0.9em;
}

/* Section Cards */
.section-card {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(15px);
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 24px;
  padding: 40px;
  margin-bottom: 40px;
  box-shadow: 0 20px 60px var(--shadow-dark);
  position: relative;
  overflow: hidden;
  animation: slideInLeft 0.8s ease-out;
}

@keyframes slideInLeft {
  from {
    opacity: 0;
    transform: translateX(-50px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

.section-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, var(--primary-blue), var(--accent-purple), var(--pink-accent), var(--cyan-accent));
  background-size: 300% 300%;
  animation: borderShimmer 3s ease infinite;
}

@keyframes borderShimmer {
  0%, 100% { background-position: 0% 50%; }
  50% { background-position: 100% 50%; }
}

.section-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
}

.section-title {
  display: flex;
  align-items: center;
  gap: 15px;
  font-size: 1.8em;
  font-weight: 700;
  color: var(--dark-gray);
  margin: 0;
}

.title-icon {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, var(--primary-blue), var(--cyan-accent));
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--white);
  animation: iconPulse 2s ease-in-out infinite;
}

@keyframes iconPulse {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.1); }
}

.title-icon svg {
  width: 20px;
  height: 20px;
}

.section-badge {
  background: linear-gradient(135deg, var(--success-green), var(--cyan-accent));
  color: var(--white);
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 0.9em;
  font-weight: 600;
  animation: badgeBounce 2s ease-in-out infinite;
}

@keyframes badgeBounce {
  0%, 100% { transform: scale(1); }
  50% { transform: scale(1.05); }
}

.section-description {
  color: var(--medium-gray);
  font-size: 1.1em;
  margin-top: 5px;
}

/* Search Controls */
.search-container {
  margin-top: 30px;
}

.search-controls {
  display: flex;
  flex-direction: column;
  gap: 20px;
  margin-bottom: 40px;
}

.search-criterion {
  display: flex;
  align-items: center;
  gap: 15px;
}

.search-label {
  font-weight: 600;
  color: var(--dark-gray);
  font-size: 1.1em;
}

.search-select {
  padding: 12px 16px;
  border: 2px solid transparent;
  border-radius: 12px;
  background: linear-gradient(var(--white), var(--white)) padding-box,
              linear-gradient(135deg, var(--primary-blue), var(--accent-purple)) border-box;
  font-size: 1em;
  font-weight: 600;
  color: var(--dark-gray);
  cursor: pointer;
  transition: all 0.3s ease;
  min-width: 160px;
}

.search-select:focus {
  outline: none;
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(37, 99, 235, 0.3);
}

.search-input-group {
  flex: 1;
}

.search-input-wrapper {
  position: relative;
  display: flex;
  background: rgba(255, 255, 255, 0.9);
  border-radius: 16px;
  border: 2px solid transparent;
  background: linear-gradient(var(--white), var(--white)) padding-box,
              linear-gradient(135deg, var(--cyan-accent), var(--primary-blue)) border-box;
  overflow: hidden;
  transition: all 0.3s ease;
}

.search-input-wrapper:focus-within {
  transform: translateY(-2px);
  box-shadow: 0 12px 40px rgba(37, 99, 235, 0.4);
  background: linear-gradient(var(--white), var(--white)) padding-box,
              linear-gradient(135deg, var(--success-green), var(--cyan-accent)) border-box;
}

.search-icon {
  position: absolute;
  left: 16px;
  top: 50%;
  transform: translateY(-50%);
  width: 20px;
  height: 20px;
  color: var(--medium-gray);
  z-index: 2;
}

.search-input {
  flex: 1;
  padding: 16px 16px 16px 50px;
  border: none;
  background: transparent;
  font-size: 1.1em;
  color: var(--dark-gray);
  outline: none;
}

.search-input::placeholder {
  color: var(--medium-gray);
  opacity: 0.7;
}

.search-btn {
  background: linear-gradient(135deg, var(--primary-blue), var(--accent-purple));
  color: var(--white);
  border: none;
  padding: 16px 30px;
  font-weight: 700;
  font-size: 1em;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.search-btn:hover {
  background: linear-gradient(135deg, var(--accent-purple), var(--pink-accent));
  transform: scale(1.05);
}

.btn-shimmer {
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent);
  transition: left 0.6s ease;
}

.search-btn:hover .btn-shimmer {
  left: 100%;
}

/* Results Section */
.results-section {
  animation: fadeIn 0.6s ease-out;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.results-header {
  margin-bottom: 25px;
}

.results-title {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 1.4em;
  font-weight: 700;
  color: var(--dark-gray);
  margin: 0;
}

.results-icon {
  width: 24px;
  height: 24px;
  color: var(--primary-blue);
}

/* Parking Lots Grid */
.parking-lots-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
  gap: 25px;
}

.parking-lot-card {
  background: rgba(255, 255, 255, 0.9);
  border-radius: 20px;
  padding: 25px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  box-shadow: 0 15px 50px var(--shadow);
  transition: all 0.4s ease;
  position: relative;
  overflow: hidden;
  animation: cardSlideIn 0.6s ease-out;
}

@keyframes cardSlideIn {
  from {
    opacity: 0;
    transform: translateY(20px) scale(0.95);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

.parking-lot-card:hover {
  transform: translateY(-8px) scale(1.02);
  box-shadow: 0 25px 80px rgba(37, 99, 235, 0.3);
  border-color: rgba(37, 99, 235, 0.4);
}

.lot-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.lot-badge {
  background: linear-gradient(135deg, var(--primary-blue), var(--accent-purple));
  color: var(--white);
  padding: 8px 16px;
  border-radius: 12px;
  font-weight: 700;
  font-size: 0.9em;
  letter-spacing: 0.5px;
}

.availability-indicator {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 6px 14px;
  border-radius: 20px;
  font-weight: 600;
  font-size: 0.9em;
}

.availability-indicator.available {
  background: rgba(16, 185, 129, 0.1);
  color: var(--success-green);
  border: 2px solid rgba(16, 185, 129, 0.3);
}

.availability-indicator.full {
  background: rgba(239, 68, 68, 0.1);
  color: var(--red-accent);
  border: 2px solid rgba(239, 68, 68, 0.3);
}

.indicator-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: currentColor;
  animation: dotPulse 2s ease-in-out infinite;
}

@keyframes dotPulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

.lot-content {
  margin-bottom: 25px;
}

.lot-address {
  display: flex;
  align-items: center;
  gap: 10px;
  font-size: 1.1em;
  font-weight: 600;
  color: var(--dark-gray);
  margin-bottom: 15px;
}

.address-icon {
  width: 18px;
  height: 18px;
  color: var(--red-accent);
}

.lot-details {
  display: flex;
  gap: 25px;
}

.detail-item {
  display: flex;
  align-items: center;
  gap: 8px;
  padding: 10px 15px;
  background: var(--light-gray);
  border-radius: 12px;
  border: 2px solid transparent;
}

.detail-item.price {
  background: linear-gradient(135deg, rgba(245, 158, 11, 0.1), rgba(236, 72, 153, 0.1));
  border-color: rgba(245, 158, 11, 0.3);
}

.detail-item.spots {
  background: linear-gradient(135deg, rgba(16, 185, 129, 0.1), rgba(6, 182, 212, 0.1));
  border-color: rgba(16, 185, 129, 0.3);
}

.detail-icon {
  width: 16px;
  height: 16px;
  color: var(--primary-blue);
}

.price-value {
  font-weight: 700;
  font-size: 1.1em;
  color: var(--accent-orange);
}

.price-unit {
  color: var(--medium-gray);
  font-size: 0.9em;
}

.spots-available {
  font-weight: 700;
  font-size: 1.1em;
  color: var(--success-green);
}

.spots-total {
  color: var(--medium-gray);
  font-size: 0.9em;
}

/* Book Button */
.book-link {
  text-decoration: none;
}

.btn-book {
  width: 100%;
  padding: 16px 24px;
  background: linear-gradient(135deg, var(--success-green), var(--cyan-accent));
  color: var(--white);
  border: none;
  border-radius: 12px;
  font-weight: 700;
  font-size: 1.1em;
  cursor: pointer;
  transition: all 0.4s ease;
  position: relative;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
}

.btn-book:disabled {
  background: linear-gradient(135deg, var(--medium-gray), var(--light-gray));
  cursor: not-allowed;
  opacity: 0.6;
}

.btn-book:not(:disabled):hover {
  background: linear-gradient(135deg, var(--cyan-accent), var(--primary-blue));
  transform: translateY(-3px);
  box-shadow: 0 15px 50px rgba(16, 185, 129, 0.4);
}

.btn-icon {
  width: 18px;
  height: 18px;
  transition: transform 0.3s ease;
}

.btn-book:hover .btn-icon {
  transform: scale(1.1);
}

/* Table Styling for Reservations */
.table-container {
  background: var(--white);
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 10px 30px var(--shadow);
}

.modern-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.95em;
}

.modern-table thead {
  background: linear-gradient(135deg, var(--primary-blue), var(--accent-purple));
  color: var(--white);
}

.modern-table th {
  padding: 18px 20px;
  text-align: left;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.5px;
  font-size: 0.85em;
}

.table-row {
  transition: all 0.3s ease;
  border-bottom: 1px solid rgba(107, 114, 128, 0.1);
}

.table-row:hover {
  background: linear-gradient(135deg, rgba(37, 99, 235, 0.05), rgba(139, 92, 246, 0.05));
  transform: scale(1.01);
}

.modern-table td {
  padding: 18px 20px;
  vertical-align: middle;
}

.lot-id-badge {
  background: linear-gradient(135deg, var(--primary-blue), var(--cyan-accent));
  color: var(--white);
  padding: 6px 12px;
  border-radius: 8px;
  font-weight: 700;
  font-size: 0.8em;
  text-align: center;
  display: inline-block;
}

.location-cell, .vehicle-cell {
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 600;
  color: var(--dark-gray);
}

.location-icon, .vehicle-icon {
  width: 16px;
  height: 16px;
  color: var(--primary-blue);
}

.status-badge {
  padding: 6px 14px;
  border-radius: 20px;
  font-weight: 600;
  font-size: 0.85em;
  text-transform: uppercase;
  letter-spacing: 0.5px;
}

.status-active {
  background: rgba(16, 185, 129, 0.1);
  color: var(--success-green);
  border: 2px solid rgba(16, 185, 129, 0.3);
}

.status-completed {
  background: rgba(107, 114, 128, 0.1);
  color: var(--medium-gray);
  border: 2px solid rgba(107, 114, 128, 0.3);
}

.btn-release {
  background: linear-gradient(135deg, var(--red-accent), var(--pink-accent));
  color: var(--white);
  border: none;
  padding: 10px 18px;
  border-radius: 10px;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  align-items: center;
  gap: 6px;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.btn-release:hover {
  background: linear-gradient(135deg, var(--pink-accent), var(--accent-purple));
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(239, 68, 68, 0.4);
}

.completed-text {
  color: var(--medium-gray);
  font-style: italic;
  font-weight: 600;
}

/* No Results */
.no-results {
  text-align: center;
  padding: 60px 40px;
  color: var(--medium-gray);
  animation: fadeIn 0.6s ease-out;
}

.no-results-icon {
  width: 80px;
  height: 80px;
  margin: 0 auto 20px;
  background: linear-gradient(135deg, var(--medium-gray), var(--light-gray));
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--white);
}

.no-results-icon svg {
  width: 40px;
  height: 40px;
}

.no-results h4 {
  font-size: 1.5em;
  font-weight: 700;
  margin-bottom: 10px;
  color: var(--dark-gray);
}

.no-results p {
  font-size: 1.1em;
  color: var(--medium-gray);
}

/* Floating Shapes */
.floating-shapes {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
  z-index: 0;
}

.shape {
  position: absolute;
  border-radius: 50%;
  opacity: 0.1;
}

.shape-1 {
  width: 100px;
  height: 100px;
  top: 15%;
  right: 10%;
  background: linear-gradient(135deg, var(--success-green), var(--cyan-accent));
  animation: floatShape1 12s ease-in-out infinite;
}

.shape-2 {
  width: 60px;
  height: 60px;
  bottom: 25%;
  left: 8%;
  background: linear-gradient(135deg, var(--accent-orange), var(--pink-accent));
  animation: floatShape2 8s ease-in-out infinite;
}

.shape-3 {
  width: 80px;
  height: 80px;
  top: 60%;
  right: 25%;
  background: linear-gradient(135deg, var(--accent-purple), var(--primary-blue));
  animation: floatShape3 10s ease-in-out infinite;
}

.shape-4 {
  width: 120px;
  height: 120px;
  bottom: 10%;
  right: 5%;
  background: linear-gradient(135deg, var(--pink-accent), var(--cyan-accent));
  animation: floatShape4 15s ease-in-out infinite;
}

@keyframes floatShape1 {
  0%, 100% { transform: translate(0, 0) rotate(0deg); }
  25% { transform: translate(30px, -20px) rotate(90deg); }
  50% { transform: translate(-15px, -35px) rotate(180deg); }
  75% { transform: translate(-25px, 15px) rotate(270deg); }
}

@keyframes floatShape2 {
  0%, 100% { transform: translate(0, 0) rotate(0deg); }
  33% { transform: translate(25px, -15px) rotate(120deg); }
  66% { transform: translate(-20px, -25px) rotate(240deg); }
}

@keyframes floatShape3 {
  0%, 100% { transform: translate(0, 0) rotate(0deg); }
  50% { transform: translate(20px, -30px) rotate(180deg); }
}

@keyframes floatShape4 {
  0%, 100% { transform: translate(0, 0) rotate(0deg); }
  25% { transform: translate(-20px, -25px) rotate(90deg); }
  50% { transform: translate(15px, -40px) rotate(180deg); }
  75% { transform: translate(30px, 10px) rotate(270deg); }
}

/* Responsive Design */
@media (max-width: 1024px) {
  .parking-lots-grid {
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
  }
  
  .nav-links {
    gap: 5px;
  }
  
  .nav-link {
    padding: 10px 15px;
    font-size: 0.9em;
  }
}

@media (max-width: 768px) {
  .main-content {
    padding: 30px 20px;
  }
  
  .section-card {
    padding: 30px 25px;
  }
  
  .welcome-title {
    font-size: 2.2em;
  }
  
  .search-controls {
    flex-direction: column;
  }
  
  .search-criterion {
    justify-content: center;
  }
  
  .parking-lots-grid {
    grid-template-columns: 1fr;
  }
  
  .lot-details {
    flex-direction: column;
    gap: 15px;
  }
  
  .stats-cards {
    flex-direction: column;
    align-items: center;
  }
  
  .nav-container {
    flex-direction: column;
    gap: 20px;
    padding: 0 20px;
  }
  
  .nav-links {
    flex-wrap: wrap;
    justify-content: center;
  }
}

@media (max-width: 480px) {
  .section-card {
    padding: 25px 20px;
  }
  
  .welcome-title {
    font-size: 1.8em;
  }
  
  .parking-lot-card {
    padding: 20px;
  }
  
  .nav-link {
    padding: 8px 12px;
    font-size: 0.85em;
  }
  
  .nav-icon {
    width: 16px;
    height: 16px;
  }
}

/* Focus States for Accessibility */
.search-btn:focus,
.search-input:focus,
.search-select:focus,
.btn-book:focus,
.btn-release:focus {
  outline: 3px solid var(--accent-orange);
  outline-offset: 2px;
}

/* Loading Animation */
.loading {
  animation: spin 1s linear infinite;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}
</style>