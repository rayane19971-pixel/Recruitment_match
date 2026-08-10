import React, { useState } from 'react';
import RadarChartCanvas from './RadarChartCanvas';
import ALL_PLAYERS from '../data/players_dataset.json';

export default function OLEffectifDashboard({ token, role }) {
  // Liste des joueurs de l'Olympique Lyonnais présents dans la base Opta 2024-2025
  const olSquad = ALL_PLAYERS.filter(p => 
    p.club && (
      p.club.includes('Lyon') || 
      p.club.includes('OL') || 
      ['Alexandre Lacazette', 'Rayane Cherki', 'Malick Fofana', 'Corentin Tolisso', 'Maxence Caqueret', 'Lucas Perri', 'Duje Ćaleta-Car', 'Moussa Niakhaté', 'Saïd Benrahma', 'Gift Orban', 'Ainsley Maitland-Niles', 'Nicolás Tagliafico', 'Clinton Mata'].includes(p.name)
    )
  );

  // Joueurs de secours si la détection par club renvoie une petite liste
  const fallbackOL = olSquad.length >= 5 ? olSquad : ALL_PLAYERS.filter(p => 
    ['Attaquant', 'Milieu'].includes(p.position)
  ).slice(0, 15);

  const [selectedOLPlayer, setSelectedOLPlayer] = useState(fallbackOL[0] || ALL_PLAYERS[0]);
  const [selectedTargetPlayer, setSelectedTargetPlayer] = useState(
    ALL_PLAYERS.find(p => p.name === 'Khvicha Kvaratskhelia' || p.name === 'Bradley Barcola' || p.name === 'Ousmane Dembélé') || ALL_PLAYERS[1]
  );
  const [targetSearchQuery, setTargetSearchQuery] = useState('');
  const [positionFilter, setPositionFilter] = useState('Tous');

  // Filtrage des candidats cibles (exclut le joueur OL sélectionné)
  const filteredTargets = ALL_PLAYERS.filter(p => {
    if (p.id === selectedOLPlayer.id) return false;
    if (positionFilter !== 'Tous' && p.position !== positionFilter) return false;
    if (targetSearchQuery.trim() !== '') {
      return p.name.toLowerCase().includes(targetSearchQuery.toLowerCase()) || 
             (p.club && p.club.toLowerCase().includes(targetSearchQuery.toLowerCase()));
    }
    return true;
  }).slice(0, 25);

  // Calcul du delta statistique entre la cible et le joueur OL
  const calcDelta = (statTarget, statOL) => {
    const diff = statTarget - statOL;
    if (diff > 0) return <span style={{ color: '#10b981', fontWeight: 800 }}>+{diff} (Gain)</span>;
    if (diff < 0) return <span style={{ color: '#ef4444', fontWeight: 800 }}>{diff}</span>;
    return <span style={{ color: '#94a3b8' }}>0 (Égal)</span>;
  };

  // Calcul de la plus-value globale (%)
  const avgOL = (selectedOLPlayer.stat_finishing + selectedOLPlayer.stat_dribbling + selectedOLPlayer.stat_passing + selectedOLPlayer.stat_pace + selectedOLPlayer.stat_defending + selectedOLPlayer.stat_physical) / 6;
  const avgTarget = (selectedTargetPlayer.stat_finishing + selectedTargetPlayer.stat_dribbling + selectedTargetPlayer.stat_passing + selectedTargetPlayer.stat_pace + selectedTargetPlayer.stat_defending + selectedTargetPlayer.stat_physical) / 6;
  const upgradePercent = Math.round(((avgTarget - avgOL) / avgOL) * 100);

  return (
    <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem' }}>
      
      {/* BANNIÈRE TITRE EFFECTIF OL */}
      <div className="glass-card" style={{ borderLeft: '5px solid #d31115' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', flexWrap: 'wrap', gap: '1rem' }}>
          <div>
            <h2 style={{ fontSize: '1.5rem', fontWeight: 800, color: '#f8fafc' }}>
              🦁 Effectif Olympique Lyonnais & Comparateur Face-à-Face 🔴🔵
            </h2>
            <p style={{ color: '#94a3b8', fontSize: '0.9rem', marginTop: '4px' }}>
              Analysez l'effectif actuel de l'OL et simulez l'impact d'une recrue d'un autre club européen.
            </p>
          </div>
          <div style={{ background: 'rgba(211, 17, 21, 0.15)', border: '1px solid rgba(211, 17, 21, 0.4)', padding: '6px 14px', borderRadius: '20px', color: '#ff4d4f', fontWeight: 800, fontSize: '0.85rem' }}>
            {fallbackOL.length} Joueurs OL Référencés
          </div>
        </div>
      </div>

      {/* SÉLECTEUR RAPIDE DE JOUEURS OL */}
      <div className="glass-card">
        <h3 style={{ fontSize: '1.05rem', fontWeight: 700, marginBottom: '0.85rem', color: '#e5a93c' }}>
          1️⃣ Choisir un Joueur de l'Effectif OL à Comparer :
        </h3>

        <div style={{ display: 'flex', gap: '0.6rem', overflowX: 'auto', paddingBottom: '0.5rem' }}>
          {fallbackOL.map(player => (
            <button
              key={player.id}
              onClick={() => setSelectedOLPlayer(player)}
              style={{
                background: selectedOLPlayer.id === player.id ? 'linear-gradient(135deg, #0b2c5c, #d31115)' : 'rgba(7, 19, 38, 0.6)',
                border: selectedOLPlayer.id === player.id ? '2px solid #e5a93c' : '1px solid rgba(255,255,255,0.08)',
                color: 'white',
                padding: '8px 14px',
                borderRadius: '10px',
                cursor: 'pointer',
                whiteSpace: 'nowrap',
                fontWeight: selectedOLPlayer.id === player.id ? 800 : 500,
                fontSize: '0.85rem',
                transition: 'all 0.2s ease',
                display: 'flex',
                alignItems: 'center',
                gap: '6px'
              }}
            >
              <span>{player.name}</span>
              <span style={{ fontSize: '0.7rem', opacity: 0.8, background: 'rgba(0,0,0,0.3)', padding: '2px 6px', borderRadius: '4px' }}>
                {player.position}
              </span>
            </button>
          ))}
        </div>
      </div>

      {/* GRILLE COMPARATIVE DUELLE (JOUEUR OL VS RECRUE CIBLE) */}
      <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '1.5rem' }}>
        
        {/* CARTE JOUEUR OL */}
        <div className="glass-card" style={{ borderTop: '4px solid #0b2c5c' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '1rem' }}>
            <div>
              <span style={{ color: '#38bdf8', fontSize: '0.75rem', fontWeight: 800, textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                🔴🔵 Titulaire OL Actuel
              </span>
              <h3 style={{ fontSize: '1.4rem', fontWeight: 900, color: 'white', marginTop: '2px' }}>
                {selectedOLPlayer.name}
              </h3>
              <p style={{ color: '#94a3b8', fontSize: '0.8rem' }}>
                {selectedOLPlayer.club || 'Olympique Lyonnais'} • {selectedOLPlayer.position} • {selectedOLPlayer.age} ans
              </p>
            </div>
            <div style={{ background: '#0b2c5c', padding: '4px 10px', borderRadius: '8px', border: '1px solid #184485', color: 'white', fontWeight: 800, fontSize: '0.9rem' }}>
              Stat {selectedOLPlayer.overall || Math.round(avgOL)}
            </div>
          </div>

          <div className="radar-canvas-container">
            <RadarChartCanvas player={selectedOLPlayer} />
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '0.5rem', background: 'rgba(5, 18, 38, 0.6)', padding: '10px', borderRadius: '10px', fontSize: '0.8rem', marginTop: '1rem' }}>
            <div><span style={{ color: '#64748b' }}>Valeur :</span> <strong>{typeof selectedOLPlayer.market_value === 'number' ? `${(selectedOLPlayer.market_value / 1000000).toFixed(1)} M €` : selectedOLPlayer.market_value}</strong></div>
            <div><span style={{ color: '#64748b' }}>Contrat :</span> <strong>{selectedOLPlayer.contract_expires || 2026}</strong></div>
            <div><span style={{ color: '#64748b' }}>Finition :</span> <strong>{selectedOLPlayer.stat_finishing}</strong></div>
            <div><span style={{ color: '#64748b' }}>Passes :</span> <strong>{selectedOLPlayer.stat_passing}</strong></div>
          </div>
        </div>

        {/* CARTE JOUEUR CIBLE (AUTRE EFFECTIF) */}
        <div className="glass-card" style={{ borderTop: '4px solid #d31115' }}>
          <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '0.5rem' }}>
            <div>
              <span style={{ color: '#ff1e23', fontSize: '0.75rem', fontWeight: 800, textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                🎯 Recrue Cible (Autre Club)
              </span>
              <h3 style={{ fontSize: '1.4rem', fontWeight: 900, color: 'white', marginTop: '2px' }}>
                {selectedTargetPlayer.name}
              </h3>
              <p style={{ color: '#94a3b8', fontSize: '0.8rem' }}>
                {selectedTargetPlayer.club} • {selectedTargetPlayer.position} • {selectedTargetPlayer.age} ans
              </p>
            </div>
            <div style={{ background: '#d31115', padding: '4px 10px', borderRadius: '8px', border: '1px solid #ff1e23', color: 'white', fontWeight: 800, fontSize: '0.9rem' }}>
              Stat {selectedTargetPlayer.overall || Math.round(avgTarget)}
            </div>
          </div>

          {/* MOTEUR DE RECHERCHE DE LA CIBLE */}
          <div style={{ marginBottom: '0.75rem', display: 'flex', gap: '0.5rem' }}>
            <input 
              type="text" 
              placeholder="Rechercher une recrue (ex: Kvaratskhelia, Barcola, Dembélé)..."
              value={targetSearchQuery}
              onChange={(e) => setTargetSearchQuery(e.target.value)}
              style={{ fontSize: '0.8rem', padding: '6px 10px' }}
            />
            <select 
              value={positionFilter} 
              onChange={(e) => setPositionFilter(e.target.value)}
              style={{ width: '110px', fontSize: '0.8rem', padding: '6px 8px' }}
            >
              <option value="Tous">Postes</option>
              <option value="Attaquant">Attaquant</option>
              <option value="Milieu">Milieu</option>
              <option value="Défenseur">Défenseur</option>
              <option value="Gardien">Gardien</option>
            </select>
          </div>

          {/* LISTE DES RÉSULTATS DES CIBLES */}
          <div style={{ display: 'flex', gap: '0.4rem', overflowX: 'auto', paddingBottom: '0.5rem', marginBottom: '0.5rem' }}>
            {filteredTargets.slice(0, 8).map(target => (
              <button
                key={target.id}
                onClick={() => setSelectedTargetPlayer(target)}
                style={{
                  background: selectedTargetPlayer.id === target.id ? '#d31115' : 'rgba(255,255,255,0.05)',
                  border: selectedTargetPlayer.id === target.id ? '1px solid #ff1e23' : '1px solid rgba(255,255,255,0.08)',
                  color: 'white',
                  padding: '4px 8px',
                  borderRadius: '6px',
                  fontSize: '0.75rem',
                  cursor: 'pointer',
                  whiteSpace: 'nowrap'
                }}
              >
                {target.name} ({target.club})
              </button>
            ))}
          </div>

          <div className="radar-canvas-container">
            <RadarChartCanvas player={selectedTargetPlayer} />
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '0.5rem', background: 'rgba(5, 18, 38, 0.6)', padding: '10px', borderRadius: '10px', fontSize: '0.8rem', marginTop: '1rem' }}>
            <div><span style={{ color: '#64748b' }}>Valeur :</span> <strong>{typeof selectedTargetPlayer.market_value === 'number' ? `${(selectedTargetPlayer.market_value / 1000000).toFixed(1)} M €` : selectedTargetPlayer.market_value}</strong></div>
            <div><span style={{ color: '#64748b' }}>Contrat :</span> <strong>{selectedTargetPlayer.contract_expires || 2026}</strong></div>
            <div><span style={{ color: '#64748b' }}>Finition :</span> <strong>{selectedTargetPlayer.stat_finishing}</strong></div>
            <div><span style={{ color: '#64748b' }}>Passes :</span> <strong>{selectedTargetPlayer.stat_passing}</strong></div>
          </div>
        </div>

      </div>

      {/* TABLEAU COMPARATIF ÉCART PAR ÉCART & BILAN DE PLUS-VALUE */}
      <div className="glass-card">
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '1rem', flexWrap: 'wrap', gap: '1rem' }}>
          <h3 style={{ fontSize: '1.2rem', fontWeight: 800, color: 'white' }}>
            📊 Bilan Comparative Opta : {selectedOLPlayer.name} vs {selectedTargetPlayer.name}
          </h3>
          <div style={{ 
            background: upgradePercent > 0 ? 'rgba(16, 185, 129, 0.15)' : 'rgba(239, 68, 68, 0.15)',
            border: `1px solid ${upgradePercent > 0 ? '#10b981' : '#ef4444'}`,
            padding: '6px 14px',
            borderRadius: '20px',
            fontWeight: 800,
            fontSize: '0.85rem',
            color: upgradePercent > 0 ? '#10b981' : '#ef4444'
          }}>
            {upgradePercent > 0 ? `▲ Plus-Value Estimée : +${upgradePercent}% de performance` : `▼ Écart Global : ${upgradePercent}%`}
          </div>
        </div>

        <table style={{ width: '100%', borderCollapse: 'collapse', textAlign: 'left', fontSize: '0.85rem' }}>
          <thead>
            <tr style={{ background: 'rgba(255,255,255,0.04)', color: '#94a3b8', textTransform: 'uppercase', fontSize: '0.75rem' }}>
              <th style={{ padding: '10px' }}>Attribut Opta</th>
              <th style={{ padding: '10px', color: '#38bdf8' }}>{selectedOLPlayer.name} (OL)</th>
              <th style={{ padding: '10px', color: '#ff1e23' }}>{selectedTargetPlayer.name} ({selectedTargetPlayer.club})</th>
              <th style={{ padding: '10px' }}>Écart / Apport Net</th>
            </tr>
          </thead>
          <tbody>
            <tr style={{ borderBottom: '1px solid rgba(255,255,255,0.05)' }}>
              <td style={{ padding: '10px', fontWeight: 700 }}>🎯 Finition (xG)</td>
              <td style={{ padding: '10px' }}>{selectedOLPlayer.stat_finishing} / 100</td>
              <td style={{ padding: '10px' }}>{selectedTargetPlayer.stat_finishing} / 100</td>
              <td style={{ padding: '10px' }}>{calcDelta(selectedTargetPlayer.stat_finishing, selectedOLPlayer.stat_finishing)}</td>
            </tr>
            <tr style={{ borderBottom: '1px solid rgba(255,255,255,0.05)' }}>
              <td style={{ padding: '10px', fontWeight: 700 }}>⚡ Dribble & Percussion</td>
              <td style={{ padding: '10px' }}>{selectedOLPlayer.stat_dribbling} / 100</td>
              <td style={{ padding: '10px' }}>{selectedTargetPlayer.stat_dribbling} / 100</td>
              <td style={{ padding: '10px' }}>{calcDelta(selectedTargetPlayer.stat_dribbling, selectedOLPlayer.stat_dribbling)}</td>
            </tr>
            <tr style={{ borderBottom: '1px solid rgba(255,255,255,0.05)' }}>
              <td style={{ padding: '10px', fontWeight: 700 }}>🅰️ Passes & xA</td>
              <td style={{ padding: '10px' }}>{selectedOLPlayer.stat_passing} / 100</td>
              <td style={{ padding: '10px' }}>{selectedTargetPlayer.stat_passing} / 100</td>
              <td style={{ padding: '10px' }}>{calcDelta(selectedTargetPlayer.stat_passing, selectedOLPlayer.stat_passing)}</td>
            </tr>
            <tr style={{ borderBottom: '1px solid rgba(255,255,255,0.05)' }}>
              <td style={{ padding: '10px', fontWeight: 700 }}>🚀 Vitesse de Pointe</td>
              <td style={{ padding: '10px' }}>{selectedOLPlayer.stat_pace} / 100</td>
              <td style={{ padding: '10px' }}>{selectedTargetPlayer.stat_pace} / 100</td>
              <td style={{ padding: '10px' }}>{calcDelta(selectedTargetPlayer.stat_pace, selectedOLPlayer.stat_pace)}</td>
            </tr>
            <tr style={{ borderBottom: '1px solid rgba(255,255,255,0.05)' }}>
              <td style={{ padding: '10px', fontWeight: 700 }}>🛡️ Défense & Tacles</td>
              <td style={{ padding: '10px' }}>{selectedOLPlayer.stat_defending} / 100</td>
              <td style={{ padding: '10px' }}>{selectedTargetPlayer.stat_defending} / 100</td>
              <td style={{ padding: '10px' }}>{calcDelta(selectedTargetPlayer.stat_defending, selectedOLPlayer.stat_defending)}</td>
            </tr>
            <tr>
              <td style={{ padding: '10px', fontWeight: 700 }}>💪 Physique & Duels</td>
              <td style={{ padding: '10px' }}>{selectedOLPlayer.stat_physical} / 100</td>
              <td style={{ padding: '10px' }}>{selectedTargetPlayer.stat_physical} / 100</td>
              <td style={{ padding: '10px' }}>{calcDelta(selectedTargetPlayer.stat_physical, selectedOLPlayer.stat_physical)}</td>
            </tr>
          </tbody>
        </table>
      </div>

    </div>
  );
}
