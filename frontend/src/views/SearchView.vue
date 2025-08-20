<template>
  <div class="search-page">
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
          
          <router-link to="/search" class="nav-link search-link active">
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
      <div class="search-container">
        <!-- Search Header -->
        <div class="search-header">
          <div class="header-content">
            <div class="title-section">
              <h1 class="page-title">
                <svg class="title-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="11" cy="11" r="8"/>
                  <path d="M21 21l-4.35-4.35"/>
                </svg>
                <span class="gradient-text">Search Dashboard</span>
              </h1>
              <p class="page-subtitle">Discover users and parking lots with intelligent search</p>
            </div>
            <div class="search-stats">
              <div class="stat-badge">
                <span class="stat-number">{{ totalResults }}</span>
                <span class="stat-label">Results Found</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Enhanced Search Controls -->
        <div class="search-controls-card">
          <div class="search-controls">
            <div class="search-type-selector">
              <label class="selector-label">Search Type</label>
              <div class="radio-group">
                <label class="radio-option" :class="{ active: criterion === 'location' }">
                  <input type="radio" v-model="criterion" value="location" />
                  <div class="radio-visual">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
                      <circle cx="12" cy="10" r="3"/>
                    </svg>
                  </div>
                  <span class="radio-text">Location</span>
                </label>
                
                <label class="radio-option" :class="{ active: criterion === 'userid' }">
                  <input type="radio" v-model="criterion" value="userid" />
                  <div class="radio-visual">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                      <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
                      <circle cx="12" cy="7" r="4"/>
                    </svg>
                  </div>
                  <span class="radio-text">User ID</span>
                </label>
              </div>
            </div>

            <div class="search-input-section">
              <div class="search-input-wrapper">
                <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <circle cx="11" cy="11" r="8"/>
                  <path d="M21 21l-4.35-4.35"/>
                </svg>
                <input
                  v-model="query"
                  @keyup.enter="doSearch"
                  type="text"
                  :placeholder="criterion === 'location' ? 'Enter location name...' : 'Enter user ID...'"
                  class="search-input"
                />
                <button @click="clearSearch" v-if="query" class="clear-btn">
                  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <line x1="18" y1="6" x2="6" y2="18"/>
                    <line x1="6" y1="6" x2="18" y2="18"/>
                  </svg>
                </button>
              </div>
              
              <button @click="doSearch" class="search-btn" :disabled="!query.trim()" :class="{ loading: isLoading }">
                <div class="btn-content">
                  <svg v-if="!isLoading" class="btn-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="11" cy="11" r="8"/>
                    <path d="M21 21l-4.35-4.35"/>
                  </svg>
                  <div v-else class="loading-spinner"></div>
                  <span>{{ isLoading ? 'Searching...' : 'Search' }}</span>
                </div>
                <div class="btn-shimmer"></div>
              </button>
            </div>
          </div>
        </div>

        <!-- Search Results -->
        <div v-if="results" class="search-results">
          <!-- Location Results -->
          <div v-if="criterion === 'location' && results?.lots?.length" class="results-section">
            <div class="results-header">
              <h2 class="results-title">
                <svg class="results-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/>
                  <circle cx="12" cy="10" r="3"/>
                </svg>
                Parking Lots Found
              </h2>
              <div class="results-count">{{ results.lots.length }} results</div>
            </div>
            <div class="results-grid">
              <ParkingDetail
                v-for="lot in results.lots"
                :key="lot.id"
                :lot="lot"
                class="result-item"
              />
            </div>
          </div>

          <!-- User Results -->
          <div v-else-if="results?.user" class="results-section">
            <div class="results-header">
              <h2 class="results-title">
                <svg class="results-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/>
                  <circle cx="12" cy="7" r="4"/>
                </svg>
                User Information
              </h2>
              <div class="results-count">1 user found</div>
            </div>
            <div class="results-grid">
              <UserInfo :user="results.user" :reservations="results.reservations" class="result-item" />
            </div>
          </div>

          <!-- No Results -->
          <div v-else class="no-results">
            <div class="no-results-content">
              <svg class="no-results-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="11" cy="11" r="8"/>
                <path d="M21 21l-4.35-4.35"/>
                <line x1="11" y1="8" x2="11" y2="14"/>
                <line x1="11" y1="16" x2="11.01" y2="16"/>
              </svg>
              <h3 class="no-results-title">No Results Found</h3>
              <p class="no-results-text">
                We couldn't find any {{ criterion === 'location' ? 'parking lots' : 'users' }} matching your search.
                Try adjusting your search terms.
              </p>
            </div>
          </div>
        </div>

        <!-- Search Suggestions -->
        <div v-if="!results && !query" class="search-suggestions">
          <div class="suggestions-card">
            <h3 class="suggestions-title">Search Tips</h3>
            <div class="suggestions-grid">
              <div class="tip-card">
                <div class="tip-icon">🏢</div>
                <h4 class="tip-title">Location Search</h4>
                <p class="tip-description">Search for parking lots by location name, address, or area</p>
              </div>
              <div class="tip-card">
                <div class="tip-icon">👤</div>
                <h4 class="tip-title">User Search</h4>
                <p class="tip-description">Find user information and reservations by entering their unique ID</p>
              </div>
              <div class="tip-card">
                <div class="tip-icon">⚡</div>
                <h4 class="tip-title">Quick Search</h4>
                <p class="tip-description">Press Enter after typing to quickly execute your search</p>
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
import axios from 'axios'
import ParkingDetail from '@/components/ParkingDetail.vue'
import UserInfo from '@/components/UserInfo.vue'

export default {
  name: 'SearchView',
  components: { 
    ParkingDetail,
    UserInfo
  },
  
  data() {
    return {
      criterion: 'location',
      query: '',
      results: null,
      isLoading: false,
      token: localStorage.getItem('token') || ''
    }
  },

  computed: {
    totalResults() {
      if (!this.results) return 0;
      if (this.results.lots) return this.results.lots.length;
      if (this.results.user) return 1;
      return 0;
    }
  },

  mounted() {
    this.token = localStorage.getItem('token') || ''
  },

  methods: {
    async doSearch() {
      if (!this.query.trim()) return;
      
      this.isLoading = true;
      this.results = null;
      console.log("🧪 Searching for:", this.query);
      
      const config = {
        headers: { 'Authentication-Token': this.token }
      };

      try {
        let resp;
        if (this.criterion === 'location') {
          resp = await axios.get('/api/parkinglot', {
            params: { query: this.query },
            ...config
          });
          this.results = {
            lots: resp.data.lots ?? resp.data
          };
          console.log('lot details', this.results.lots)
        } else {
          resp = await axios.get(`/api/search/userinfo/${this.query}`, {
            params: { query: this.query },
            ...config
          });
          const raw = resp.data.data ?? {};
          const {
            reservations = [],
            ...userDetails
          } = raw;
          this.results = {
            user: userDetails,
            reservations
          };
        }
      } catch (error) {
        console.error("Search failed:", error);
        this.results = null;
      } finally {
        this.isLoading = false;
      }
    },

    clearSearch() {
      this.query = '';
      this.results = null;
    }
  }
}
</script>

<style scoped>
/* Color Variables - Matching Dashboard Theme */
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

.search-page {
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

/* Background Pattern */
.bg-pattern {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: 
    radial-gradient(circle at 20% 20%, rgba(255, 255, 255, 0.05) 0%, transparent 50%),
    radial-gradient(circle at 80% 80%, rgba(245, 158, 11, 0.05) 0%, transparent 50%),
    radial-gradient(circle at 60% 40%, rgba(139, 92, 246, 0.05) 0%, transparent 50%);
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

/* Navigation Bar - Matching Dashboard */
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

.search-link.active,
.search-link:hover { 
  background: linear-gradient(135deg, var(--cyan-accent), var(--success-green));
  color: var(--white);
  box-shadow: 0 4px 15px rgba(6, 182, 212, 0.3);
}

.home-link:hover { background: linear-gradient(135deg, var(--primary-blue), var(--secondary-blue)); }
.users-link:hover { background: linear-gradient(135deg, var(--accent-purple), var(--pink-accent)); }
.summary-link:hover { background: linear-gradient(135deg, var(--accent-orange), var(--pink-accent)); }
.logout-link:hover { background: linear-gradient(135deg, var(--red-accent), var(--pink-accent)); }

/* Main Content */
.main-content {
  position: relative;
  z-index: 1;
  padding: 40px 20px;
}

.search-container {
  max-width: 1000px;
  margin: 0 auto;
}

/* Search Header */
.search-header {
  margin-bottom: 40px;
}

.header-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 20px;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(15px);
  padding: 30px;
  border-radius: 20px;
  box-shadow: 0 15px 50px var(--shadow);
  border: 2px solid transparent;
  background-clip: padding-box;
  position: relative;
}

.header-content::before {
  content: '';
  position: absolute;
  inset: 0;
  padding: 2px;
  background: linear-gradient(135deg, var(--cyan-accent), var(--success-green), var(--accent-orange));
  border-radius: inherit;
  mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  mask-composite: exclude;
  -webkit-mask-composite: xor;
}

.title-section {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.page-title {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 2.2em;
  font-weight: 800;
  margin: 0;
  color: var(--dark-gray);
}

.title-icon {
  width: 36px;
  height: 36px;
  color: var(--cyan-accent);
  animation: searchIconRotate 4s ease-in-out infinite;
}

@keyframes searchIconRotate {
  0%, 100% { transform: rotate(0deg); }
  50% { transform: rotate(15deg); }
}

.gradient-text {
  background: linear-gradient(135deg, var(--primary-blue), var(--cyan-accent));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.page-subtitle {
  color: var(--medium-gray);
  font-size: 1.1em;
  font-weight: 500;
  margin: 0;
}

.search-stats {
  display: flex;
  align-items: center;
}

.stat-badge {
  background: linear-gradient(135deg, var(--success-green), var(--cyan-accent));
  color: var(--white);
  padding: 12px 20px;
  border-radius: 12px;
  text-align: center;
  box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3);
}

.stat-number {
  display: block;
  font-size: 1.4em;
  font-weight: 800;
}

.stat-label {
  font-size: 0.8em;
  opacity: 0.9;
  font-weight: 600;
}

/* Search Controls Card */
.search-controls-card {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(15px);
  border-radius: 20px;
  padding: 30px;
  margin-bottom: 30px;
  box-shadow: 0 15px 50px var(--shadow);
  border: 2px solid transparent;
  background-clip: padding-box;
  position: relative;
  overflow: hidden;
}

.search-controls-card::before {
  content: '';
  position: absolute;
  inset: 0;
  padding: 2px;
  background: linear-gradient(135deg, var(--primary-blue), var(--accent-purple), var(--pink-accent));
  background-size: 300% 300%;
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

.search-controls {
  display: flex;
  flex-direction: column;
  gap: 25px;
}

/* Search Type Selector */
.search-type-selector {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.selector-label {
  font-size: 1.1em;
  font-weight: 700;
  color: var(--dark-gray);
}

.radio-group {
  display: flex;
  gap: 15px;
  flex-wrap: wrap;
}

.radio-option {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 15px 20px;
  background: rgba(243, 244, 246, 0.5);
  border: 2px solid transparent;
  border-radius: 12px;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.radio-option input[type="radio"] {
  display: none;
}

.radio-visual {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background: var(--light-gray);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
}

.radio-visual svg {
  width: 16px;
  height: 16px;
  color: var(--medium-gray);
  transition: color 0.3s ease;
}

.radio-text {
  font-weight: 600;
  color: var(--medium-gray);
  transition: color 0.3s ease;
}

.radio-option.active {
  background: linear-gradient(135deg, rgba(37, 99, 235, 0.1), rgba(6, 182, 212, 0.1));
  border-color: var(--primary-blue);
  transform: translateY(-2px);
  box-shadow: 0 8px 25px rgba(37, 99, 235, 0.2);
}

.radio-option.active .radio-visual {
  background: linear-gradient(135deg, var(--primary-blue), var(--cyan-accent));
}

.radio-option.active .radio-visual svg,
.radio-option.active .radio-text {
  color: var(--white);
}

.radio-option.active .radio-text {
  color: var(--primary-blue);
  font-weight: 700;
}

/* Search Input Section */
.search-input-section {
  display: flex;
  gap: 15px;
  align-items: flex-end;
}

.search-input-wrapper {
  flex: 1;
  position: relative;
  display: flex;
  align-items: center;
}

.search-icon {
  position: absolute;
  left: 15px;
  width: 20px;
  height: 20px;
  color: var(--medium-gray);
  z-index: 2;
}

.search-input {
  width: 100%;
  padding: 15px 15px 15px 45px;
  border: 2px solid var(--light-gray);
  border-radius: 12px;
  font-size: 1em;
  font-weight: 500;
  background: rgba(255, 255, 255, 0.8);
  transition: all 0.3s ease;
  outline: none;
}

.search-input:focus {
  border-color: var(--cyan-accent);
  background: var(--white);
  box-shadow: 0 0 0 3px rgba(6, 182, 212, 0.1);
  transform: translateY(-2px);
}

.clear-btn {
  position: absolute;
  right: 10px;
  width: 30px;
  height: 30px;
  border: none;
  background: var(--medium-gray);
  color: var(--white);
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  z-index: 2;
}

.clear-btn:hover {
  background: var(--red-accent);
  transform: scale(1.1);
}

.clear-btn svg {
  width: 14px;
  height: 14px;
}

/* Search Button */
.search-btn {
  background: linear-gradient(135deg, var(--cyan-accent), var(--success-green));
  color: var(--white);
  padding: 15px 30px;
  border: none;
  border-radius: 12px;
  font-weight: 700;
  font-size: 1em;
  cursor: pointer;
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
  box-shadow: 0 8px 32px rgba(6, 182, 212, 0.3);
  min-width: 120px;
}

.search-btn:hover {
  transform: translateY(-3px) scale(1.05);
  box-shadow: 0 15px 60px rgba(6, 182, 212, 0.5);
}

.search-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
  transform: none;
  box-shadow: 0 4px 15px rgba(6, 182, 212, 0.2);
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

.search-btn:hover .btn-icon {
  transform: rotate(90deg);
}

.loading-spinner {
  width: 18px;
  height: 18px;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-top: 2px solid var(--white);
  border-radius: 50%;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
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

.search-btn:hover .btn-shimmer {
  left: 100%;
}

/* Search Results */
.search-results {
  animation: slideInUp 0.6s ease-out;
}

@keyframes slideInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.results-section {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(15px);
  border-radius: 20px;
  padding: 30px;
  box-shadow: 0 15px 50px var(--shadow);
  border: 2px solid transparent;
  background-clip: padding-box;
  position: relative;
}

.results-section::before {
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

.results-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 25px;
  padding-bottom: 20px;
  border-bottom: 2px solid var(--light-gray);
}

.results-title {
  display: flex;
  align-items: center;
  gap: 12px;
  font-size: 1.5em;
  font-weight: 700;
  color: var(--dark-gray);
  margin: 0;
}

.results-icon {
  width: 24px;
  height: 24px;
  color: var(--success-green);
}

.results-count {
  background: linear-gradient(135deg, var(--accent-orange), var(--pink-accent));
  color: var(--white);
  padding: 8px 16px;
  border-radius: 20px;
  font-size: 0.9em;
  font-weight: 600;
  box-shadow: 0 4px 15px rgba(245, 158, 11, 0.3);
}

.results-grid {
  display: grid;
  gap: 20px;
}

.result-item {
  animation: fadeInScale 0.6s ease-out;
  transition: all 0.3s ease;
}

.result-item:hover {
  transform: translateY(-5px);
  box-shadow: 0 20px 60px var(--shadow-dark);
}

@keyframes fadeInScale {
  from {
    opacity: 0;
    transform: scale(0.95);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

/* No Results */
.no-results {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(15px);
  border-radius: 20px;
  padding: 60px 30px;
  text-align: center;
  box-shadow: 0 15px 50px var(--shadow);
  border: 2px solid transparent;
  background-clip: padding-box;
  position: relative;
  animation: slideInUp 0.6s ease-out;
}

.no-results::before {
  content: '';
  position: absolute;
  inset: 0;
  padding: 2px;
  background: linear-gradient(135deg, var(--medium-gray), var(--light-gray));
  border-radius: inherit;
  mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  mask-composite: exclude;
  -webkit-mask-composite: xor;
}

.no-results-content {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 15px;
}

.no-results-icon {
  width: 64px;
  height: 64px;
  color: var(--medium-gray);
  opacity: 0.7;
}

.no-results-title {
  font-size: 1.5em;
  font-weight: 700;
  color: var(--dark-gray);
  margin: 0;
}

.no-results-text {
  color: var(--medium-gray);
  font-size: 1.1em;
  line-height: 1.6;
  max-width: 400px;
  margin: 0;
}

/* Search Suggestions */
.search-suggestions {
  animation: fadeIn 0.8s ease-out;
}

@keyframes fadeIn {
  from { opacity: 0; }
  to { opacity: 1; }
}

.suggestions-card {
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(15px);
  border-radius: 20px;
  padding: 40px;
  box-shadow: 0 15px 50px var(--shadow);
  border: 2px solid transparent;
  background-clip: padding-box;
  position: relative;
}

.suggestions-card::before {
  content: '';
  position: absolute;
  inset: 0;
  padding: 2px;
  background: linear-gradient(135deg, var(--accent-purple), var(--pink-accent), var(--accent-orange));
  background-size: 300% 300%;
  border-radius: inherit;
  mask: linear-gradient(#fff 0 0) content-box, linear-gradient(#fff 0 0);
  mask-composite: exclude;
  -webkit-mask-composite: xor;
  animation: borderFlow 8s ease infinite;
}

.suggestions-title {
  text-align: center;
  font-size: 1.8em;
  font-weight: 700;
  color: var(--dark-gray);
  margin: 0 0 30px 0;
  background: linear-gradient(135deg, var(--accent-purple), var(--pink-accent));
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.suggestions-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 25px;
}

.tip-card {
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.1), rgba(243, 244, 246, 0.1));
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 16px;
  padding: 25px;
  text-align: center;
  transition: all 0.3s ease;
  backdrop-filter: blur(10px);
}

.tip-card:hover {
  transform: translateY(-8px) scale(1.02);
  box-shadow: 0 20px 60px var(--shadow-dark);
  background: linear-gradient(135deg, rgba(255, 255, 255, 0.2), rgba(243, 244, 246, 0.2));
}

.tip-icon {
  font-size: 2.5em;
  margin-bottom: 15px;
  display: block;
}

.tip-title {
  font-size: 1.2em;
  font-weight: 700;
  color: var(--dark-gray);
  margin: 0 0 10px 0;
}

.tip-description {
  color: var(--medium-gray);
  line-height: 1.5;
  margin: 0;
  font-size: 0.95em;
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
  .header-content {
    flex-direction: column;
    text-align: center;
    gap: 25px;
  }
  
  .page-title {
    font-size: 2em;
  }
  
  .search-input-section {
    flex-direction: column;
    align-items: stretch;
    gap: 15px;
  }
  
  .search-btn {
    width: 100%;
  }
}

@media (max-width: 768px) {
  .nav-links {
    flex-wrap: wrap;
    gap: 5px;
    justify-content: center;
  }
  
  .nav-link {
    padding: 10px 15px;
    font-size: 0.9em;
  }
  
  .main-content {
    padding: 30px 15px;
  }
  
  .search-controls-card,
  .header-content,
  .results-section,
  .suggestions-card {
    padding: 25px 20px;
  }
  
  .page-title {
    font-size: 1.8em;
  }
  
  .radio-group {
    justify-content: center;
  }
  
  .suggestions-grid {
    grid-template-columns: 1fr;
    gap: 20px;
  }
}

@media (max-width: 480px) {
  .nav-container {
    flex-direction: column;
    gap: 15px;
    padding: 0 15px;
  }
  
  .main-content {
    padding: 20px 10px;
  }
  
  .search-controls-card,
  .header-content,
  .results-section,
  .suggestions-card {
    padding: 20px 15px;
    border-radius: 16px;
  }
  
  .page-title {
    font-size: 1.6em;
    flex-direction: column;
    text-align: center;
    gap: 8px;
  }
  
  .radio-group {
    flex-direction: column;
    align-items: stretch;
  }
  
  .radio-option {
    justify-content: center;
  }
  
  .search-input {
    padding: 12px 12px 12px 40px;
  }
  
  .search-btn {
    padding: 12px 20px;
  }
}

/* Focus States for Accessibility */
.nav-link:focus,
.radio-option:focus-within,
.search-input:focus,
.search-btn:focus,
.clear-btn:focus {
  outline: 3px solid var(--accent-orange);
  outline-offset: 2px;
}

/* High Contrast Mode Support */
@media (prefers-contrast: high) {
  .search-controls-card,
  .header-content,
  .results-section,
  .suggestions-card {
    border: 2px solid var(--dark-gray);
  }
  
  .radio-option.active {
    border-color: var(--dark-gray);
    background: var(--primary-blue);
    color: var(--white);
  }
}

/* Reduced Motion Support */
@media (prefers-reduced-motion: reduce) {
  .search-page,
  .bg-pattern,
  .float-shape,
  .brand-icon,
  .title-icon,
  .search-controls-card::before,
  .suggestions-card::before {
    animation: none;
  }
  
  .search-btn:hover,
  .radio-option.active,
  .tip-card:hover,
  .result-item:hover {
    transform: none;
  }
}

/* Print Styles */
@media print {
  .floating-elements,
  .bg-pattern {
    display: none;
  }
  
  .search-page {
    background: white;
  }
  
  .search-controls-card,
  .header-content,
  .results-section {
    box-shadow: none;
    border: 1px solid #ccc;
  }
}
</style>