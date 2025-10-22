# User Data Directory

**Purpose:** Centralized storage for all user-specific data, configurations, and agent-managed content.

## Directory Structure

```
user-data/
├── secrets.env                  # Private configuration (NEVER commit to git)
├── inventory/                   # Inventory agent data
│   ├── en-disponibilidad.md    # Current inventory
│   ├── ideal-y-necesario.md    # Essential items list
│   ├── agotado.md              # Depleted items
│   └── deseado.md              # Wish list
├── ideas/                       # Ideas agent data
│   └── knowledge-graph.md      # Knowledge graph structure
└── knowledge/                   # Knowledge base and documentation
    ├── index.md                # Documentation index
    ├── errores.md              # Error documentation
    └── [other documentation files]
```

## Configuration File: `secrets.env`

**CRITICAL:** This file contains sensitive information and is excluded from version control via `.gitignore`.

### Setup Instructions

1. Copy `.env.example` from project root to `user-data/secrets.env`
2. Update values with your actual credentials and paths
3. Verify `user-data/secrets.env` is listed in `.gitignore`
4. Never commit this file to git

### Environment Variables

The `secrets.env` file defines:

- **SUDO_PASSWORD**: System sudo password for authenticated operations
- **USER_DATA_BASE_PATH**: Base path for all user data (default: `user-data`)
- **INVENTORY_BASE_PATH**: Inventory agent data location
- **IDEAS_BASE_PATH**: Ideas agent data location
- **KNOWLEDGE_BASE_PATH**: Knowledge base location
- Individual file paths for each agent's managed files

## Security

- All sensitive data MUST be stored in `secrets.env`
- Agent files reference paths via environment variables (`${VARIABLE_NAME}`)
- No hardcoded credentials in agent configuration files
- `.gitignore` ensures `secrets.env` is never versioned

## Adding New Agents

When creating a new agent that needs to store data:

1. Create subdirectory under `user-data/` (e.g., `user-data/new-agent/`)
2. Add environment variables to `secrets.env`:
   ```bash
   NEW_AGENT_BASE_PATH=${USER_DATA_BASE_PATH}/new-agent
   NEW_AGENT_FILE_1=${NEW_AGENT_BASE_PATH}/file1.md
   ```
3. Update `.env.example` with placeholder values
4. Document new paths in this README
5. Configure agent to use environment variables for paths

## Migration Notes

**Date:** 2025-10-21

This directory structure was created as part of architectural refactoring to:
- Centralize all user data in one location
- Separate sensitive data from version control
- Enable flexible path configuration via environment variables
- Improve security and portability

**Previous Structure:**
- `Inventario/` → migrated to `user-data/inventory/`
- `ideas/` → migrated to `user-data/ideas/`
- `documentacion/` → migrated to `user-data/knowledge/`

All agent configuration files were updated to reference new paths dynamically via environment variables.
