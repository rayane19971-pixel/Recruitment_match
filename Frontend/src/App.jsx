import React, { useState, useEffect } from 'react';
import LoginModal from './components/LoginModal';
import PlayerRadarModal from './components/PlayerRadarModal';
import BudgetDashboard from './components/BudgetDashboard';
import ScoutingFilters from './components/ScoutingFilters';
import PlayerSearchBar from './components/PlayerSearchBar';
import OLEffectifDashboard from './components/OLEffectifDashboard';
import ALL_PLAYERS from './data/players_dataset.json';

export default function App() {

  const [token, setToken] = useState(localStorage.getItem('ol_jwt_token') || '');
  const [role, setRole] = useState(localStorage.getItem('ol_user_role') || '');
  const [username, setUsername] = useState(localStorage.getItem('ol_username') || '');
  
  const [activeTab, setActiveTab] = useState('scouting');
  const [players, setPlayers] = useState([]);
  const [loading, setLoading] = useState(false);
  const [selectedPlayer, setSelectedPlayer] = useState(null);

  const handleLoginSuccess = (newToken, newRole, newUsername) => {
    setToken(newToken);
    setRole(newRole);
    setUsername(newUsername);
    localStorage.setItem('ol_jwt_token', newToken);
    localStorage.setItem('ol_user_role', newRole);
    localStorage.setItem('ol_username', newUsername);
  };

  const handleLogout = () => {
    setToken('');
    setRole('');
    setUsername('');
    localStorage.removeItem('ol_jwt_token');
    localStorage.removeItem('ol_user_role');
    localStorage.removeItem('ol_username');
  };

  // Fonction de recherche (API Backend local avec fallback client-side immédiat)
  const handleSearch = (filters) => {
    if (!token) return;
    setLoading(true);

    let url = `http://127.0.0.1:8000/players/search?finishing=${filters.finishing}&dribbling=${filters.dribbling}&passing=${filters.passing}&pace=${filters.pace}&defending=${filters.defending}&physical=${filters.physical}&max_age=${filters.maxAge}&max_contract_year=${filters.maxContractYear}`;
    
    if (filters.maxMarketValue && filters.maxMarketValue < 200) {
      url += `&max_market_value=${filters.maxMarketValue * 1000000}`;
    }
    if (filters.position !== 'Tous') {
      url += `&position=${encodeURIComponent(filters.position)}`;
    }

    fetch(url, {
      headers: {
        'Authorization': `Bearer ${token}`
      }
    })
      .then(res => {
        if (!res.ok) throw new Error("API non disponible");
        return res.json();
      })
      .then(data => {
        if (data && data.joueurs) {
          setPlayers(data.joueurs);
        }
        setLoading(false);
      })
      .catch(err => {
        // Mode Fallback Client-side si le serveur Python local n'est pas démarré
        console.warn("API Python locale absente, calcul du matching côté client sur les 2,854 joueurs Opta");
        
        let filtered = ALL_PLAYERS.filter(p => {
          if (filters.position !== 'Tous' && p.position !== filters.position) return false;
          if (p.age > filters.maxAge) return false;
          if (p.contract_expires > filters.maxContractYear) return false;
          if (filters.maxMarketValue && filters.maxMarketValue < 200 && typeof p.market_value === 'number' && p.market_value > (filters.maxMarketValue * 1000000)) return false;
          return true;
        });

        filtered = filtered.map(p => {
          const diffSq = (
            Math.pow(p.stat_finishing - filters.finishing, 2) +
            Math.pow(p.stat_dribbling - filters.dribbling, 2) +
            Math.pow(p.stat_passing - filters.passing, 2) +
            Math.pow(p.stat_pace - filters.pace, 2) +
            Math.pow(p.stat_defending - filters.defending, 2) +
            Math.pow(p.stat_physical - filters.physical, 2)
          );
          const distance = Math.sqrt(diffSq / 6);
          const matchScore = Math.round(Math.max(0, 100 - distance) * 10) / 10;
          
          const copy = { ...p, match_score: matchScore, score_compatibilite: `${matchScore}%` };
          
          if (role === 'scout') {
            copy.market_value = "Confidentiel (Réservé Direction)";
            copy.wage = "Confidentiel (Réservé Direction)";
          }
          return copy;
        });

        filtered.sort((a, b) => b.match_score - a.match_score);
        setPlayers(filtered.slice(0, 100));
        setLoading(false);
      });
  };

  // Recherche initiale une seule fois au chargement
  useEffect(() => {
    if (token) {
      handleSearch({
        position: 'Tous',
        maxAge: 40,
        maxContractYear: 2030,
        finishing: 40,
        dribbling: 40,
        passing: 40,
        pace: 40,
        defending: 30,
        physical: 40
      });
    }
  }, [token]);

  if (!token) {
    return (
      <div className="app-container" style={{ justifyContent: 'center', alignItems: 'center' }}>
        <LoginModal onLoginSuccess={handleLoginSuccess} />
      </div>
    );
  }

  return (
    <div className="app-container">
      {/* NAVBAR */}
      <header className="navbar">
        <div className="brand-section">
          <img src="/ol_logo.png" alt="OL Logo" style={{ width: '50px', height: '55px', marginRight: '15px', borderRadius: '5px' }} />
          <div className="brand-title">
            RECRUITMENT MATCH
            <span className="brand-subtitle">Olympique Lyonnais • Data Intelligence</span>
          </div>
        </div>

        <div className="nav-links">
          <button 
            className={`nav-btn ${activeTab === 'scouting' ? 'active' : ''}`}
            onClick={() => setActiveTab('scouting')}
          >
            🎛️ Scouting & Matching
          </button>
          <button 
            className={`nav-btn ${activeTab === 'effectif' ? 'active' : ''}`}
            onClick={() => setActiveTab('effectif')}
          >
            🦁 Effectif OL & Comparateur
          </button>
          <button 
            className={`nav-btn ${activeTab === 'budget' ? 'active' : ''}`}
            onClick={() => setActiveTab('budget')}
          >
            💰 Budget Mercato
          </button>
        </div>

        <div className="user-profile">
          <span className={`role-badge role-${role}`}>
            {role}
          </span>
          <span style={{ fontSize: '0.85rem', fontWeight: 600 }}>{username}</span>
          <button className="btn-logout" onClick={handleLogout}>
            Déconnexion
          </button>
        </div>
      </header>

      {/* MAIN CONTENT */}
      <main className="main-content">
        {activeTab === 'effectif' ? (
          <OLEffectifDashboard token={token} role={role} onSelectPlayer={(p) => setSelectedPlayer(p)} />
        ) : activeTab === 'budget' ? (
          <BudgetDashboard token={token} role={role} />
        ) : (
          <div className="scouting-grid">
            {/* COMPOSANT ISOLÉ DE CURSEURS OPTA (Ne fait plus ramer la grille !) */}
            <ScoutingFilters onSearch={handleSearch} loading={loading} />

            {/* GRILLE DES RÉSULTATS JOUEURS */}
            <div>
              {/* BARRE DE RECHERCHE DIRECTE PAR NOM DE JOUEUR */}
              <PlayerSearchBar token={token} onSelectPlayer={(p) => setSelectedPlayer(p)} />

              <div className="results-header">
                <div>
                  <h2 style={{ fontSize: '1.3rem', fontWeight: 800 }}>Joueurs Compatibles (2,854 Joueurs Opta 2024-2025)</h2>
                  <p className="results-count">Triés par ordre décroissant de compatibilité (%)</p>
                </div>
                <span style={{ fontSize: '0.85rem', color: '#10b981', fontWeight: 700 }}>
                  {players.length} résultat{players.length > 1 ? 's' : ''} trouvé{players.length > 1 ? 's' : ''}
                </span>
              </div>

              {loading ? (
                <div style={{ textAlign: 'center', padding: '3rem', color: '#94a3b8' }}>
                  Calcul du Matching Opta en cours...
                </div>
              ) : players.length === 0 ? (
                <div className="glass-card" style={{ textAlign: 'center', padding: '3rem', color: '#94a3b8' }}>
                  Aucun joueur ne correspond aux filtres stricts sélectionnés.
                </div>
              ) : (
                <div className="players-grid">
                  {players.map((p) => {
                    const scoreNum = p.match_score || 0;
                    const badgeClass = scoreNum >= 80 ? '' : scoreNum >= 65 ? 'medium' : 'low';

                    return (
                      <div key={p.id} className="player-card">
                        <div className="card-top">
                          <div>
                            <div className="player-name">{p.name}</div>
                            <div className="player-club">{p.club} • {p.position}</div>
                          </div>
                          <span className={`match-badge ${badgeClass}`}>
                            {p.score_compatibilite || `${scoreNum}%`}
                          </span>
                        </div>

                        <div className="player-meta">
                          <div className="meta-item">
                            <span>Âge & Nat.</span>
                            <strong>{p.age} ans ({p.nationality})</strong>
                          </div>
                          <div className="meta-item">
                            <span>Fin Contrat</span>
                            <strong style={{ color: p.contract_expires <= 2026 ? '#f59e0b' : 'white' }}>
                              {p.contract_expires}
                            </strong>
                          </div>
                          <div className="meta-item" style={{ gridColumn: 'span 2' }}>
                            <span>Valeur / Salaire</span>
                            <strong>
                              {typeof p.market_value === 'number'
                                ? `${(p.market_value / 1000000).toFixed(1)} M € (${(p.wage / 1000000).toFixed(2)} M€/an)`
                                : <span className="confidential-tag">{p.market_value}</span>}
                            </strong>
                          </div>
                        </div>

                        <div className="opta-mini-stats">
                          <div className="stat-box">
                            <span className="val">{p.stat_finishing}</span>
                            <span className="lbl">FIN</span>
                          </div>
                          <div className="stat-box">
                            <span className="val">{p.stat_dribbling}</span>
                            <span className="lbl">DRI</span>
                          </div>
                          <div className="stat-box">
                            <span className="val">{p.stat_passing}</span>
                            <span className="lbl">PAS</span>
                          </div>
                          <div className="stat-box">
                            <span className="val">{p.stat_pace}</span>
                            <span className="lbl">VIT</span>
                          </div>
                          <div className="stat-box">
                            <span className="val">{p.stat_defending}</span>
                            <span className="lbl">DEF</span>
                          </div>
                          <div className="stat-box">
                            <span className="val">{p.stat_physical}</span>
                            <span className="lbl">PHY</span>
                          </div>
                        </div>

                        <button className="btn-card-action" onClick={() => setSelectedPlayer(p)}>
                          📊 Fiche & Graphique Radar
                        </button>
                      </div>
                    );
                  })}
                </div>
              )}
            </div>
          </div>
        )}
      </main>

      {/* MODAL RADAR & DETAILS */}
      {selectedPlayer && (
        <PlayerRadarModal 
          player={selectedPlayer} 
          token={token} 
          onClose={() => setSelectedPlayer(null)} 
          onSelectPlayer={(sim) => setSelectedPlayer(sim)}
        />
      )}
    </div>
  );
}
