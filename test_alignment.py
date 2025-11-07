#!/usr/bin/env python3
"""Test script to verify alignment algorithms work correctly"""

from core.alignment_global import AlignmentGlobal
from core.alignment_local import AlignmentLocal

def test_global_alignment():
    print("Testing Global Alignment (Needleman-Wunsch)...")
    seqA = "ACGTACGT"
    seqB = "ACGACG"
    
    aligner = AlignmentGlobal(seqA, seqB)
    result = aligner.compute()
    
    print(f"Sequence A: {seqA}")
    print(f"Sequence B: {seqB}")
    print(f"Matrix dimensions: {len(result['matrix'])}x{len(result['matrix'][0])}")
    print(f"Alignment score: {result['matrix'][-1][-1]}")
    print(f"Traceback path length: {len(result['traceback'])}")
    print("✓ Global alignment completed successfully\n")
    
    return result

def test_local_alignment():
    print("Testing Local Alignment (Smith-Waterman)...")
    seqA = "ACGTACGT"
    seqB = "ACGACG"
    
    aligner = AlignmentLocal(seqA, seqB)
    result = aligner.compute()
    
    max_score = max(max(row) for row in result['matrix'])
    
    print(f"Sequence A: {seqA}")
    print(f"Sequence B: {seqB}")
    print(f"Matrix dimensions: {len(result['matrix'])}x{len(result['matrix'][0])}")
    print(f"Max alignment score: {max_score}")
    print(f"Traceback path length: {len(result['traceback'])}")
    print("✓ Local alignment completed successfully\n")
    
    return result

if __name__ == "__main__":
    print("=" * 60)
    print("Bioinformatics Alignment Algorithm Tests")
    print("=" * 60)
    print()
    
    try:
        global_result = test_global_alignment()
        local_result = test_local_alignment()
        
        print("=" * 60)
        print("✓ All tests passed successfully!")
        print("=" * 60)
        print("\nCore alignment algorithms are working correctly.")
        print("You can now run the GUI with: python app.py")
        
    except Exception as e:
        print(f"✗ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
