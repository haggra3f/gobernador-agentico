# Error Knowledge Base

**Purpose:** Centralized repository of errors, their resolutions, and preventive patterns.

**Maintained by:** error-documenter agent

**Last Updated:** 2025-10-21

---

## How to Use This Document

### Searching for Errors
- Use Grep with error message, symptoms, or domain tags
- Example: `Grep pattern="#mcp-tools" path="documentacion/errores.md"`
- Search by ERROR-ID if you know the specific error number

### Adding New Errors
- Invoke error-documenter agent with error details
- Agent will check for duplicates and apply Synthesis Protocol
- NEVER manually add errors - always use error-documenter

### Error Entry Format
Each error follows standardized structure:
- ERROR-ID: Unique sequential identifier
- Date, Domain, Severity, Status
- Symptoms, Root Cause, Context
- Resolution steps (actionable)
- Prevention guidance
- Related errors (cross-references)
- Tags for searchability

---

## Error Patterns

**Common Patterns Identified:**
(This section is automatically updated by error-documenter when patterns are detected)

*No patterns identified yet - error knowledge base is new.*

---

## Error Entries

### ERROR-001: Direct Read of Agent-Owned File Violating Encapsulation

**Date:** 2025-10-21 14:30 UTC
**Domain:** Agent Coordination / System Architecture
**Severity:** High
**Status:** Resolved

#### Symptoms
- Main thread directly read `orchestrator.md` using Read tool
- Main thread manually parsed orchestrator.md to extract execution counters
- Bypassed orchestrator agent entirely when querying orchestrator state

#### Root Cause
**Policy Violation:** Violated Agent Encapsulation Policy (CLAUDE.md lines 535-573)

**What Happened:**
User asked: "¿Cómo está el contador de ejecuciones de microagentes?"

Instead of invoking orchestrator agent to report its own state, main thread:
1. Used `Read(/mnt/d/Proyectos/Gobernador agentico/.claude/agents/orchestrator.md)`
2. Used `Grep` to search for specific counters
3. Manually parsed and presented the information

**What Should Have Happened:**
1. Invoke orchestrator agent
2. Ask: "Dame el estado de los contadores de ejecución de todos los micro-agentes"
3. Orchestrator returns information in structured format from its own authoritative source

#### Context
This occurred shortly after implementing the Agent Encapsulation Policy (2025-10-21), which establishes:
- Agent files belong to their respective agents
- Never manually read/update agent files - always invoke the agent
- Each agent is authoritative source for its domain

The policy was explicitly modeled after inventory-librarian encapsulation but applies system-wide:
- `orchestrator.md` → orchestrator agent
- `inventario/*.md` → inventory-librarian agent
- `ideas/knowledge-graph.md` → ideas agent
- etc.

#### Technical Details

**Incorrect Actions Taken:**
```bash
# ❌ WRONG: Direct file access
Read(/mnt/d/Proyectos/Gobernador agentico/.claude/agents/orchestrator.md)
Grep pattern="execution_count" path=".claude/agents/orchestrator.md"
# Manual parsing and presentation
```

**Correct Approach:**
```bash
# ✅ CORRECT: Agent invocation
Skill command="orchestrator"
# Ask: "Report execution counters for all micro-agents"
# Orchestrator returns structured data
```

**Policy Violated:**
CLAUDE.md lines 545-550 establishes:
> "NEVER manually update inventory files - ALWAYS invoke inventory-librarian"

Similar principle applies universally:
> "NEVER read orchestrator.md directly - ALWAYS ask orchestrator"

#### Consequences

1. **Encapsulation Broken:** orchestrator.md is orchestrator's domain, not main thread's
2. **Fragility Created:** Changes to orchestrator.md internal format break direct-read code
3. **Logic Duplication:** Reimplemented functionality that orchestrator already provides
4. **Bad Precedent:** Contradicts recently-implemented policy, sets wrong example

#### Resolution

**Immediate Action:**
- User pointed out policy violation
- Error recognized and acknowledged
- Committed to correct approach for future queries

**Correct Implementation Going Forward:**
```
User: "¿Cómo está el contador de ejecuciones de microagentes?"
Main Thread:
  1. Invoke orchestrator agent
  2. Request: "Report current execution counters for all micro-agents"
  3. Present orchestrator's structured response to user
```

#### Prevention Guidance

**Decision Tree for File Access:**

Before reading ANY file, ask:
1. **"Is this file owned by a specific agent?"**
   - orchestrator.md → YES (orchestrator)
   - inventario/*.md → YES (inventory-librarian)
   - ideas/knowledge-graph.md → YES (ideas)
   - CLAUDE.md → YES (desarrollador for modifications)
   - documentacion/errores.md → YES (error-documenter)

2. **If YES:**
   - ✅ INVOKE the agent
   - ❌ NEVER read directly

3. **If NO (general documentation, user files, etc.):**
   - ✅ Read directly is fine

**Key Principle:**
> "Each agent is the authoritative interface to its own data. Never bypass the interface by accessing data directly."

**Analogy:**
Just like you wouldn't directly read a database file instead of using SQL queries, don't read agent files instead of invoking agents.

**Quick Reference:**
| File Pattern | Owner Agent | Action |
|--------------|-------------|--------|
| `.claude/agents/orchestrator.md` | orchestrator | Invoke orchestrator |
| `inventario/*.md` | inventory-librarian | Invoke inventory-librarian |
| `ideas/knowledge-graph.md` | ideas | Invoke ideas |
| `documentacion/errores.md` | error-documenter | Invoke error-documenter |
| `.claude/CLAUDE.md` | desarrollador (for edits) | Invoke desarrollador |
| `plan.md`, `project-tracking.md` | desarrollador | Invoke desarrollador |
| General `documentacion/*.md` | None (unless specific) | Read directly OK |

#### Related Errors
- None yet (ERROR-001 is first documented error)
- This establishes pattern for future agent encapsulation violations

#### Tags
`#agent-encapsulation` `#policy-violation` `#orchestrator` `#architecture` `#best-practices` `#high-severity`

---

### ERROR-002: Triple Violation - Direct Git Execution + Incorrect Error Documentation

**Date:** 2025-10-21
**Domain:** Agent Coordination / Routing / System Architecture
**Severity:** Critical
**Status:** Resolved

#### Symptoms
- Main thread executed git/GitHub commands directly (git add, git commit, gh repo create)
- Main thread bypassed orchestrator agent for routing decision
- Main thread used ideas agent to document system error instead of error-documenter agent
- System error (#005) added to user's knowledge-graph.md (wrong domain)

#### Root Cause
**Triple Policy Violation:**

1. **Agent Encapsulation Policy** (CLAUDE.md lines 544-571)
   - Git/GitHub operations are exclusive domain of github-manager agent
   - Main thread executed commands directly instead of delegating

2. **Routing Strategy** (CLAUDE.md lines 481-484)
   - CLAUDE.md should categorize, orchestrator should route
   - Main thread made tactical routing decision without authority

3. **Complex Routing Rule** (CLAUDE.md lines 503-516)
   - Task didn't match 3 direct routing patterns
   - Should have delegated to orchestrator
   - Main thread bypassed orchestrator entirely

**What Happened:**
```
User: "guarda este proyecto en github"

Main Thread (INCORRECT):
  ❌ Executed git add . directly
  ❌ Executed git commit -m "..." directly
  ❌ Executed gh repo create ... directly
  ❌ Then used ideas agent to document the error
  ❌ Added system error to user's knowledge graph
```

**What Should Have Happened:**
```
User: "guarda este proyecto en github"

Main Thread (CORRECT):
  1. Identify category: development (git/GitHub operations)
  2. Check routing patterns: Not in 3 direct patterns
  3. Delegate to orchestrator

Orchestrator:
  4. Analyze request: git/GitHub domain
  5. Route to github-manager agent

github-manager:
  6. Execute git/gh commands with proper protocol
  7. Return result

Main Thread:
  8. Report completion to user
```

#### Context
This error occurred shortly after the orchestrator architecture was implemented (2025-10-21), which established clear separation:
- CLAUDE.md: Strategic coordination (categories)
- Orchestrator: Tactical routing (specific agent selection)
- Specialized agents: Domain execution (github-manager for git/GitHub)

The triple violation represents a fundamental misunderstanding of architectural layers:
1. **Execution layer** violation: Bypassed github-manager
2. **Routing layer** violation: Bypassed orchestrator
3. **Documentation layer** violation: Used wrong agent for error capture

#### Technical Details

**Incorrect Flow:**
```
User request
    ↓
Main thread directly:
  - git add .
  - git commit -m "..."
  - gh repo create ...
    ↓
Main thread invokes ideas agent
    ↓
System error added to knowledge-graph.md
```

**Correct Flow:**
```
User request
    ↓
Main thread → Orchestrator
    ↓
Orchestrator → github-manager
    ↓
github-manager → git/gh commands
    ↓
Result to user

(Later, if error occurred)
Main thread → error-documenter
    ↓
Error added to errores.md
```

**Root Causes Identified:**
1. **False Sense of Simplicity:** "It's just git commands" → Bypassed architecture
2. **Performance Optimization Bias:** Saved 50-100ms → Corrupted system integrity
3. **Incomplete Rule Internalization:** Rules existed but weren't applied automatically
4. **No Pre-execution Validation:** No gate asking "Does this belong to an agent?"

#### Consequences

**Immediate Impact:**
- Task completed (apparent success) but violated 3 critical architectural principles
- Created dangerous precedent for future violations
- Demonstrated weakness in rule enforcement

**Long-term Risk:**
```
1 violation → Normalization of bypass behavior
    ↓
Multiple violations → Gradual architectural erosion
    ↓
Fragmented system → Multiple inconsistent execution paths
    ↓
Unmaintainable chaos → System integrity compromised
```

**Specific Risks:**
- Git operations sometimes through github-manager, sometimes direct → Inconsistent logs
- Orchestrator bypassed → Routing system weakened
- System errors in user's knowledge graph → Domain confusion
- Future developers learn wrong patterns → Propagation of violations

#### Resolution

**Immediate Actions Taken:**
1. Recognized the triple violation
2. Documented error using error-documenter agent (this entry)
3. Will remove ERROR entry #005 from ideas/knowledge-graph.md
4. Reinforced understanding of architectural layers

**Correct Implementation for Future:**
```
Before executing ANY tool/command:

QUESTION 1: Domain Ownership Check
- Does this belong to an agent's domain?
  - git/GitHub ops → github-manager
  - inventory → inventory-librarian
  - email → gmail-manager
  - ideas → ideas agent
  - errors → error-documenter

If YES → STOP and delegate to agent

QUESTION 2: Routing Authority Check
- Is this one of 3 direct routing patterns?
  - "Compré [item]" → inventory-librarian
  - "Se acabó [item]" → inventory-librarian
  - "Manda email" → gmail-manager

If NO → Delegate to orchestrator for routing decision

QUESTION 3: Error Documentation Check
- Is this documenting an error?
  - System error → error-documenter agent
  - User idea → ideas agent
```

#### Prevention Guidance

**Pre-execution Validation Checklist:**

Before ANY execution, validate:

```
┌─────────────────────────────────────────────┐
│ EXECUTION VALIDATION GATE                   │
├─────────────────────────────────────────────┤
│ 1. Domain Check:                            │
│    ❓ Does operation belong to agent domain?│
│    ✅ YES → Delegate to agent               │
│    ❌ NO  → Continue to routing check       │
│                                             │
│ 2. Routing Check:                           │
│    ❓ Is this direct routing pattern?       │
│    ✅ YES → Execute direct pattern          │
│    ❌ NO  → Delegate to orchestrator        │
│                                             │
│ 3. Authority Check:                         │
│    ❓ Do I have authority for this?         │
│    ✅ YES → Proceed with execution          │
│    ❌ NO  → STOP and delegate               │
└─────────────────────────────────────────────┘
```

**Red Flags That Indicate Imminent Violation:**
1. "This is simple, I can just..." → STOP
2. "Faster if I skip the agent..." → STOP
3. "User wants speed, not architecture..." → STOP
4. "Just this once..." → STOP
5. "Orchestrator is overkill for..." → STOP
6. No explicit CLAUDE.md reference before execution → STOP

**Key Principles:**
- **Encapsulation is Absolute:** No exceptions for "simple" operations
- **Routing System Exists for Reason:** 50ms saved vs. infinite debugging cost
- **Simplicity ≠ Authority:** Simple tasks still go through proper channels
- **Architecture > Speed:** Consistency is more valuable than micro-optimizations

#### Related Errors
- **Related to ERROR-001:** Both are agent encapsulation violations
- **Extends ERROR-001:** ERROR-001 was read violation, ERROR-002 is execution + routing + documentation violation
- **Pattern Emerging:** Agent encapsulation violations (2 occurrences)

#### Tags
`#agent-encapsulation` `#routing-violation` `#orchestrator-bypass` `#github-manager` `#git-operations` `#architecture` `#critical-severity` `#policy-violation` `#triple-violation` `#ideas-agent-misuse`

---

## Error Patterns

**Common Patterns Identified:**

### Pattern #1: Agent Encapsulation Violations (2 occurrences)
- ERROR-001: Direct read of orchestrator.md
- ERROR-002: Direct execution of git commands + routing bypass

**Common Root Cause:** False sense of simplicity or speed optimization
**Prevention:** Implement pre-execution validation gate
**Recommendation:** Reinforce that encapsulation applies to ALL operations, regardless of perceived simplicity

---

## Statistics

**Total Errors Documented:** 2
**Critical:** 1
**High:** 1
**Medium:** 0
**Low:** 0

**Most Common Domains:**
- Agent Coordination / System Architecture: 2

**Most Common Error Types:**
- Agent Encapsulation Violation: 2
- Policy Violation: 2
- Routing Violation: 1

**Error Pattern Detection:**
- Agent Encapsulation Pattern: 2 occurrences (threshold for systematic review)

---

**Note:** This knowledge base grows over time. Each documented error makes future problem-solving faster and helps prevent recurrence.
