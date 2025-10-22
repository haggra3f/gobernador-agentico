# CLAUDE.md Evolution History

Esta es la historia completa de evoluciones del sistema de directivas.

## Version 1.7 (2025-10-21)
- Created orchestrator agent (.claude/agents/orchestrator.md) with complete agent coordination logic
- Extracted ~200+ lines of agent routing protocols from CLAUDE.md to orchestrator.md
- Reduced CLAUDE.md from 47,126 chars (766 lines) to 33,612 chars (542 lines) = 28.7% reduction
- Achieved target size: <40,000 chars (6,388 chars under target)
- Replaced detailed agent_usage guideline with simplified agent_coordination guideline
- Implemented hybrid routing model: direct patterns (99% cases) + orchestrator (complex cases)
- Preserved all core principles, user meta-directives, and critical functionality
- New agent registry includes orchestrator for intelligent routing and multi-agent coordination
- All agent coordination logic (selection protocol, approval delegation, registry) now in orchestrator.md
- System more modular: routing rules can evolve without touching CLAUDE.md

## Version 1.6 (2025-10-18)
- Clarified token formula: removed ambiguous "Baseline %" term
- Standardized XML attributes: critical_file_protection uses priority="critical"
- Added status="mandatory" to synthesis_protocol for consistency
- Added failure_handling to backup_creation phase (safety)
- Added early_exit_clause to synthesis_planning (flexibility)
- Evolution improvements: 1.6% document change (12 lines)

## Version 1.5 (2025-10-18)
- Added automatic backup creation phase to *evoluciona* command
- Backup created before every evolution with timestamp in .claude/backups/
- Added backup_safety rule to meta_evolution section
- Ensures safe rollback capability for all evolution operations

## Version 1.4 (2025-10-18)
- Corrected token usage rate from 0.33% to 0.52% per 1K tokens (verified with user data)
- Re-calibrated token rate to 0.39% based on total usage data (67K = 26%)
- Fixed conversation token limit from 300K to 200K in format string
- Updated verification note to reflect accurate calibration data
- Removed obsolete reference to plan_before_execute principle in preservation_check

## Version 1.3 (2025-10-17)
- Delegated complex development workflow to "desarrollador" agent
- Removed plan_before_execute principle (now in desarrollador agent)
- Simplified workflow_process to delegation reference (~44 lines → 7 lines)
- Simplified state_management to reference (~43 lines → 9 lines)
- Removed code_generation_limits and task_complexity_check (in desarrollador)
- Simplified token_usage_tracking to core rules (~84 lines → 8 lines)
- Cleaned redundant execution_guidelines (~20 lines removed)
- Total reduction: ~30% (778 lines → ~550 lines)
- Core focus: Agent coordination + reflexive capabilities (*recuerda*, *evoluciona*)

## Version 1.2 (2025-10-16)
- Consolidated redundant synthesis protocols through intelligent referencing
- Unified token reporting requirements for clarity
- Standardized XML attribute system (priority/status)
- Generalized token rate guidance, removed session-specific data
- Consolidated file operation rules with cross-references
