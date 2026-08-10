import React, { useState } from 'react';
import ALL_PLAYERS from '../data/players_dataset.json';

export default function OLEffectifDashboard({ onSelectPlayer, role }) {
  const [selectedPosition, setSelectedPosition] = useState('Tous');
  const [searchQuery, setSearchQuery] = useState('');

  // Liste des joueurs de l'Olympique Lyonnais dans le dataset
  const olSquadRaw = ALL_PLAYERS.filter(p => 
    p.club && (
      p.club.includes('Lyon') || 
      p.club.includes('OL') || 
      ['Alexandre Lacazette', 'Rayane Cherki', 'Malick Fofana', 'Corentin Tolisso', 'Maxence Caqueret', 'Lucas Perri', 'Duje Ćaleta-Car', 'Moussa Niakhaté', 'Saïd Benrahma', 'Gift Orban', 'Ainsley Maitland-Niles', 'Nicolás Tagliafico', 'Clinton Mata', 'Tanner Tessmann', 'Georges Mikautadze', 'Abner Vinícius', 'Jordan Veretout', 'Warmed Omari', 'Ernest Nuamah'].includes(p.name)
    )
  );

  // Fallback si la détection stricte renvoie une courte liste
  const olSquad = olSquadRaw.length >= 8 ? olSquadRaw : ALL_PLAYERS.slice(0, 20);

  // Filtres par secteur de jeu et par nom
  const filteredSquad = olSquad.filter(player => {
    if (selectedPosition !== 'Tous' && player.position !== selectedPosition) return false;
    if (searchQuery.trim() !== '') {
      return player.name.toLowerCase().includes(searchQuery.toLowerCase());
    }
    return true;
  });

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
      
      {/* BANNIÈRE TITRE EFFECTIF OL */}
      <div className="glass-card" style={{ borderLeft: '5px solid #d31115' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '1rem' }}>
          <div>
            <h2 style={{ fontSize: '1.5rem', fontWeight: 800, color: '#f8fafc' }}>
              🦁 Effectif de l'Olympique Lyonnais 🔴🔵
            </h2>
            <p style={{ color: '#94a3b8', fontSize: '0.9rem', marginTop: '4px' }}>
              Cliquez sur la fiche de n'importe quel joueur lyonnais pour ouvrir son radar et découvrir ses <strong>Jumeaux Statistiques (KNN)</strong> dans les 5 grands championnats.
            </p>
          </div>
          <div style={{ background: 'rgba(211, 17, 21, 0.15)', border: '1px solid rgba(211, 17, 21, 0.4)', padding: '6px 14px', borderRadius: '20px', color: '#ff4d4f', fontWeight: 800, fontSize: '0.85rem' }}>
            {filteredSquad.length} Joueurs OL Sélectionnés
          </div>
        </div>
      </div>

      {/* BARRE DE FILTRES ET RECHERCHE AU SEIN DE L'EFFECTIF */}
      <div className="glass-card" style={{ display: 'flex', gap: '1rem', alignItems: 'center', flexWrap: 'wrap' }}>
        <div style={{ flex: 1, minWidth: '220px' }}>
          <input 
            type="text" 
            placeholder="Rechercher un joueur lyonnais (ex: Cherki, Lacazette, Fofana)..."
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            style={{ padding: '8px 12px', fontSize: '0.85rem' }}
          />
        </div>

        <div style={{ display: 'flex', gap: '0.5rem' }}>
          {['Tous', 'Attaquant', 'Milieu', 'Défenseur', 'Gardien'].map(pos => (
            <button
              key={pos}
              onClick={() => setSelectedPosition(pos)}
              style={{
                background: selectedPosition === pos ? 'linear-gradient(135deg, #0b2c5c, #d31115)' : 'rgba(255,255,255,0.05)',
                border: selectedPosition === pos ? '1px solid #e5a93c' : '1px solid rgba(255,255,255,0.08)',
                color: 'white',
                padding: '6px 12px',
                borderRadius: '8px',
                fontWeight: selectedPosition === pos ? 800 : 500,
                fontSize: '0.8rem',
                cursor: 'pointer',
                transition: 'all 0.2s ease'
              }}
            >
              {pos}
            </button>
          ))}
        </div>
      </div>

      {/* GRILLE DES CARTES DE JOUEURS DE L'EFFECTIF OL */}
      <div className="players-grid">
        {filteredSquad.map(player => {
          const avgOverall = Math.round(
            (player.stat_finishing + player.stat_dribbling + player.stat_passing + player.stat_pace + player.stat_defending + player.stat_physical) / 6
          );

          return (
            <div 
              key={player.id} 
              className="player-card"
              onClick={() => onSelectPlayer(player)}
              style={{ cursor: 'pointer', borderTop: '3px solid #d31115' }}
            >
              <div className="card-top">
                <div>
                  <h3 className="player-name">{player.name}</h3>
                  <span className="player-club">{player.club || 'Olympique Lyonnais'}</span>
                </div>
                <span className="match-badge">
                  {player.position}
                </span>
              </div>

              <div className="player-meta">
                <div className="meta-item">
                  <span>Âge</span>
                  <strong>{player.age} ans</strong>
                </div>
                <div className="meta-item">
                  <span>Valeur</span>
                  <strong>
                    {role === 'scout' ? 'Confidentiel' : (typeof player.market_value === 'number' ? `${(player.market_value / 1000000).toFixed(1)} M €` : player.market_value)}
                  </strong>
                </div>
              </div>

              {/* MINI RADAR PREVIEW (3 CLÉS OPТА) */}
              <div className="opta-mini-stats">
                <div className="stat-box">
                  <span className="val">{player.stat_finishing}</span>
                  <span className="lbl">FINITION</span>
                </div>
                <div className="stat-box">
                  <span className="val">{player.stat_dribbling}</span>
                  <span className="lbl">DRIBBLE</span>
                </div>
                <div className="stat-box">
                  <span className="val">{player.stat_passing}</span>
                  <span className="lbl">PASSES</span>
                </div>
              </div>

              <button className="btn-card-action">
                🔍 Voir Radar & Jumeaux Statistiques (KNN)
              </button>
            </div>
          );
        })}
      </div>

    </div>
  );
}
